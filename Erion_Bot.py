#!/usr/bin/env python2
# -*- coding: utf8 -*-

import irclib
import ircbot
import re

class BotModeration(ircbot.SingleServerIRCBot):
    def __init__(self):
        """
        Constructeur qui pourrait prendre des paramètres dans un "vrai" programme.
        """
        ircbot.SingleServerIRCBot.__init__(self, [("chat.freenode.net", 6667)],
                                           "Erion_Bot", "Bot de modération réalisé en Python avec ircbot")
        self.insultes = ["con", "pute"] # Liste à agrandir pour un "vrai" programme.
        self.commandes =["!voice","!kick"]
        self.users = ["Hideyuki","Ufeseros","Xathote","Tsumenokage"]
    def on_welcome(self, serv, ev):
        """
        Méthode appelée une fois connecté et identifié.
        Notez qu'on ne peut rejoindre les canaux auparavant.
        """
        serv.join("#Erion")

    def on_pubmsg(self, serv, ev):
        """
        Méthode appelée à la réception d'un message, qui exclut son expéditeur s'il
        écrit une insulte.
        """
        # Il n'est pas indispensable de passer par des variables
        # Ici elles permettent de clarifier le tout.
        auteur = irclib.nm_to_n(ev.source())
        canal = ev.target()
        message = ev.arguments()[0]
        
        if re.match(r"^!voice", message) is not None:
            serv.privmsg(canal, "Ceci est un test");
            reponse = message.replace("!voice","")
            serv.mode(canal,"+v"+reponse)
            

    def on_join(self, serv, ev):
        """
        Méthode sui va se déclencher a la connextion d'un utilisateur
        """

        for user in self.users:
            if(ev.source == user):
                serv.mode(canal,"+v"+ev.source)
        
        
if __name__ == "__main__":
    BotModeration().start()
