from pyrogram import Client, filters
import json

app = Client("trama bot")

@app.on_message(filters.command("help"))
async def help(_, message):
    text="Los comandos disponibles son los siguientes:\n"\
    "/help Muestra la ayuda\n"\
    "/listaTramas Muestra cada Persona con su número de tramas\n"\
    "/addTrama + @usuario: Añade en 1 la cuenta de las tramas del usuario mencionado"\
    "/quitTrama + @usuario: Elimina en 1 la cuenta de las tramas del usuario mencionado"    
    await app.send_message(message.chat.id,text)

@app.on_message(filters.command("start"))
async def start(_, message):
    await app.send_message(message.chat.id,"Bienvenido al TramaBot no hay K-RDMM que se escape\nEstoy en fase alfa tened paciencia queda mucho por implementar")

#Command to send to the group the number of tramas for each person
@app.on_message(filters.command("listaTramas"))
async def listaTrama(_, message):
    chat_id=message.chat.id
    text=""
    with open('tramas.json', 'r') as openfile: 
        # Reading from json file
        pjson = json.loads(openfile.read())
    people=pjson["People"]
    #Send the number of tramas to the group of each person 
    for p in people:
        text+="@"+str(p["Nombre"])+" Ha tramado "+str(p["Tramas"])+" veces\n"
    await app.send_message(chat_id,text)

#Command to add a trama to someone specific
@app.on_message(filters.command("addTrama"))
async def addTrama(_, message):
    chat_id=message.chat.id
    text=message.text
    try:
        name=text.split('@')[1] #Name of the person 
        with open('tramas.json', 'r') as openfile: 
        # Reading from json file
            pjson = json.loads(openfile.read())
        people=pjson["People"]
        enc=0
        i=0
        while(enc==0 and i< len(people)):
            if(people[i]["Nombre"]==name):
                enc=1
                people[i]["Tramas"]+=1
            else:
                i+=1
        if (enc==0):
            await app.send_message(chat_id,"Usuario no encontrado prueba de nuevo")
        else:
            pjson["People"]=people
            # Writing to tramas.json
        with open("tramas.json", "w") as outfile:
            outfile.write(json.dumps(pjson,indent=2))
        await listaTrama(_,message)
    #If the format in telegram is not correct raise this exception
    except IndexError:
        await app.send_message(chat_id,"Formato incorrecto prueba de nuevo")
        name="none"

@app.on_message(filters.command("quitTrama"))
async def addTrama(_, message):
    chat_id=message.chat.id
    text=message.text
    try:
        name=text.split('@')[1] #Name of the person 
        with open('tramas.json', 'r') as openfile: 
        # Reading from json file
            pjson = json.loads(openfile.read())
        people=pjson["People"]
        enc=0
        i=0
        while(enc==0 and i< len(people)):
            if(people[i]["Nombre"]==name):
                enc=1
                people[i]["Tramas"]-=1
            else:
                i+=1
        if (enc==0):
            await app.send_message(chat_id,"Usuario no encontrado prueba de nuevo")
        else:
            pjson["People"]=people
            # Writing to tramas.json
        with open("tramas.json", "w") as outfile:
            outfile.write(json.dumps(pjson,indent=2))
        await listaTrama(_,message)
    #If the format in telegram is not correct raise this exception
    except IndexError:
        await app.send_message(chat_id,"Formato incorrecto prueba de nuevo")
        name="none"
    
    

    '''
    await app.send_message(chat_id,"¿Quien ha tramado esta vez?")
    async for member in app.get_chat_members(chat_id):
        user=member.user
        user_id=user.id
        user_name=user.first_name
        user_last_name=user.last_name
        username=user.username
        print(str(user_id)+" "+username+" "+user_name)
        await app.send_message(chat_id,username+"\n")
        '''
app.run()