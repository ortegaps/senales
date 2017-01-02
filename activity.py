#!/usr/bin/env python



import random
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from ConfigParser import SafeConfigParser
import logging



class Base:
    def __init__(self):
        self.window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        self.window.connect("delete-event", Gtk.main_quit)
        
        #Parser
        parser=SafeConfigParser()
        parser.read('Config.ini')   
        ram = random.randint(1,6)
        #Widgets
        win=Gtk.EventBox()
        win.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse('White'))

        menu=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        title=Gtk.Label('Senales de transito')
        inicio=Gtk.Image()
        conoce=Gtk.Button(parser.get('botones','a'))
        sabes=Gtk.Button(parser.get('botones','b'))
        sabias=Gtk.Button(parser.get('botones','c'))
        salir=Gtk.Button(parser.get('botones','e'))
        #self.fondo = gtk.EventBox()
        #self.fondo.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('White'))



    
        #Conexiones
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/inicio.gif', 400, 400)
        inicio.set_from_pixbuf(pixbuf)
        conoce.connect('clicked', self.conoceme, menu, win)
        sabes.connect('clicked', self.initi, menu, win)
        sabias.connect('clicked', self.futurista, menu, win, ram,)



        #Diseno
        self.window.add(win)
        win.add(menu)
        menu.add(title)
        menu.add(inicio)
        menu.add(conoce)
        menu.add(sabes)
        menu.add(sabias)	
        self.window.show_all()

    def conoceme(self, conoce, menu=None, win=None):
    	win.remove(menu)
        conociendo=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        informativas=Gtk.Frame(label='Informativas')
        informativas.set_shadow_type(Gtk.ShadowType.ETCHED_OUT)
        informativas.set_size_request(400, 700)
        preventivas=Gtk.Frame(label='Preventivas')
        preventivas.set_shadow_type(Gtk.ShadowType.ETCHED_OUT)
        preventivas.set_size_request(400, 700)
        reglamentarias = Gtk.Frame(label='Reglamentarias')
        reglamentarias.set_shadow_type(Gtk.ShadowType.ETCHED_OUT)
        reglamentarias.set_size_request(400, 700) 
    
    #Conexiones
        bbox = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL)
        bbox.set_layout(Gtk.ButtonBoxStyle.CENTER)
        
        salir = Gtk.Button('Inicio')

        salir.connect('clicked', self.salir, menu, win, conociendo)


        infomage=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        infomage1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        infomage2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        infomage3=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        win.add(conociendo)
        conociendo.add(informativas)
        conociendo.add(preventivas)
        conociendo.add(reglamentarias)
        self.scrolled_informativas = Gtk.ScrolledWindow()
        self.scrolled_informativas.set_border_width(10)
        self.scrolled_informativas.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        informativas.add(self.scrolled_informativas)
        self.scrolled_informativas.add_with_viewport(infomage)
        preventivasimg=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        preventivasimg1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        preventivasimg2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        preventivasimg3=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.scrolled_preventivas = Gtk.ScrolledWindow()
        self.scrolled_preventivas.set_border_width(10)
        self.scrolled_preventivas.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        preventivas.add(self.scrolled_preventivas)
        self.scrolled_preventivas.add_with_viewport(preventivasimg)
        reglamentariasV1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        reglamentariasH1=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        reglamentariasV2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        reglamentariasV3=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        reglamentariasV4=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.scrolled_reglamentarias = Gtk.ScrolledWindow()
        self.scrolled_reglamentarias.set_border_width(10)
        self.scrolled_reglamentarias.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        reglamentarias.add(self.scrolled_reglamentarias)
        self.scrolled_reglamentarias.add_with_viewport(reglamentariasV1)
        reglamentariasV1.add(reglamentariasH1)
        reglamentariasH1.add(reglamentariasV2)
        reglamentariasH1.add(reglamentariasV3)
        reglamentariasH1.add(reglamentariasV4)
        win.show()

        #Labels para completar los verticals y que sean todas iguales 
        a=Gtk.Label()
        b=Gtk.Label()
        f=Gtk.Label()
        g=Gtk.Label()
        h=Gtk.Label()
        
            #Imagenes informativas
        #Desde aqui se encuentran las imagenes de las senales de transito informativas, 
        #divididas en partes para que todo sea organizado en 4 Verticals Box
        #aeropuerto 
        aeropuerto=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/aeropuerto.gif', 24, 24)
        aeropuerto.set_from_pixbuf(pixbuf)
        aeropuertob=Gtk.Button()
        aeropuertob.add(aeropuerto)
        aeropuertob.connect('clicked', self.detalle, conociendo, salir, win, 'aeropuerto')
        #balneario
        balneario=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/balneario.gif', 24, 24)
        balneario.set_from_pixbuf(pixbuf)
        balneariob=Gtk.Button()
        balneariob.add(balneario)
        balneariob.connect('clicked', self.detalle, conociendo, salir, win, 'balneario')
        #bar
        bar=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/bar.gif', 24, 24)
        bar.set_from_pixbuf(pixbuf)
        barb=Gtk.Button()
        barb.add(bar)
        barb.connect('clicked', self.detalle, conociendo, salir, win, 'Bar')
        #camino sin salida
        css=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/camino-o-calle-sin-salida.gif', 24, 24)
        css.set_from_pixbuf(pixbuf)
        cssb=Gtk.Button()
        cssb.add(css)
        cssb.connect('clicked', self.detalle, conociendo, salir, win, 'camino_sin_salida')
        #camino sin salida 2
        css2=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/camino-o-calle-sin-salida2.gif', 24, 24)
        css2.set_from_pixbuf(pixbuf)
        css2b=Gtk.Button()
        css2b.add(css2)
        css2b.connect('clicked', self.detalle, conociendo, salir, win, 'camino_sin_salida2')
        #paso transitable 
        pt=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/paso1.gif', 24, 24)
        
        pt.set_from_pixbuf(pixbuf)
        ptb=Gtk.Button()
        ptb.add(pt)
        ptb.connect('clicked', self.detalle, conociendo, salir, win, 'camino_transitable')
        # camino-o-paso-transitable2
        pt2=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/paso2.gif', 24, 24)
        pt2.set_from_pixbuf(pixbuf)
        pt2b=Gtk.Button()
        pt2b.add(pt2)
        pt2b.connect('clicked', self.detalle, conociendo, salir, win, 'camino-o-paso-transitable2')
        #campamento
        campamento=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/campamento.gif', 24, 24)
        campamento.set_from_pixbuf(pixbuf)
        campamentob=Gtk.Button()
        campamentob.add(campamento)
        campamentob.connect('clicked', self.detalle, conociendo, salir, win, 'campamento')
        #comienzo de autopista
        cda=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/comienzo-de-autopista.gif', 24, 24)
        cda.set_from_pixbuf(pixbuf)
        cdab=Gtk.Button()
        cdab.add(cda)
        cdab.connect('clicked', self.detalle, conociendo, salir, win, 'comienzo_de_autopista')
        #correo
        correo=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/correo.gif', 24, 24)
        
        correo.set_from_pixbuf(pixbuf)
        correob=Gtk.Button()
        correob.add(correo)
        correob.connect('clicked', self.detalle, conociendo, salir, win, 'correo')
        
        #desvio por cambio de sentido
        dcs=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/desvio-por-cambio-de-sentid.gif', 24, 24)
        
        dcs.set_from_pixbuf(pixbuf)
        dcsb=Gtk.Button()
        dcsb.add(dcs)
        dcsb.connect('clicked', self.detalle, conociendo, salir, win, 'desvio_por_cambio_de_sentido')
        #direcciones permitidas
        dp1=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/direccione2s-permitidad-igu.gif', 24, 24)
        
        dp1.set_from_pixbuf(pixbuf)
        dp1b=Gtk.Button()
        dp1b.add(dp1)
        dp1b.connect('clicked', self.detalle, conociendo, salir, win, 'direcciones_permitidas')
        #direcciones permitidas2
        dp2=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/direcciones-permitidad-am-s.gif', 24, 24)
        
        dp2.set_from_pixbuf(pixbuf)
        dp2b=Gtk.Button()
        dp2b.add(dp2)
        dp2b.connect('clicked', self.detalle, conociendo, salir, win, 'direcciones_permitidas2')
        #direcciones permitidas3
        dp3=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/direcciones-permitidad-bifu.gif', 24, 24)
        
        dp3.set_from_pixbuf(pixbuf)
        dp3b=Gtk.Button()
        dp3b.add(dp3)
        dp3b.connect('clicked', self.detalle, conociendo, salir, win, 'direcciones_permitidas3')
        #direcciones permitidas4
        dp4=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/direcciones-permitidad-dere.gif', 24, 24)
        
        dp4.set_from_pixbuf(pixbuf)
        dp4b=Gtk.Button()
        dp4b.add(dp4)
        dp4b.connect('clicked', self.detalle, conociendo, salir, win, 'direcciones_permitidas4')
        #direcciones permitidas5
        dp5=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/direcciones-permitidad-igua.gif', 24, 24)
        
        dp5.set_from_pixbuf(pixbuf)
        dp5b=Gtk.Button()
        dp5b.add(dp5)
        dp5b.connect('clicked', self.detalle, conociendo, salir, win, 'direcciones_permitidas5')
        #direcciones permitidas6
        dp6=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/direcciones-permitidad-izqu.gif', 24, 24)
        
        dp6.set_from_pixbuf(pixbuf)
        dp6b=Gtk.Button()
        dp6b.add(dp6)
        dp6b.connect('clicked', self.detalle, conociendo, salir, win, 'direcciones_permitidas6')
        #esquema de recorrido
        edr=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/esquema-de-recorrido.gif', 24, 24)
        
        edr.set_from_pixbuf(pixbuf)
        edrb=Gtk.Button()
        edrb.add(edr)
        edrb.connect('clicked', self.detalle, conociendo, salir, win, 'esquema_de_recorrido')
        #estacionamiento
        estacionamiento=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/estacionamiento.gif', 24, 24)
        
        estacionamiento.set_from_pixbuf(pixbuf)
        estacionamientob=Gtk.Button()
        estacionamientob.add(estacionamiento)
        estacionamientob.connect('clicked', self.detalle, conociendo, salir, win, 'estacionamiento')
        
        #estacionamiento de casas rodantes
        estacionamiento2=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/estacionamiento-de-casas-ro.gif', 24, 24)
        
        estacionamiento2.set_from_pixbuf(pixbuf)
        estacionamiento2b=Gtk.Button()
        estacionamiento2b.add(estacionamiento2)
        estacionamiento2b.connect('clicked', self.detalle, conociendo, salir, win, 'estacionamiento_de_casas_ro')
        #estacionamiento permitido
        estacionamiento3=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/estacionamiento-permitido.gif', 24, 24)
        
        estacionamiento3.set_from_pixbuf(pixbuf)
        estacionamiento3b=Gtk.Button()
        estacionamiento3b.add(estacionamiento3)
        estacionamiento3b.connect('clicked', self.detalle, conociendo, salir, win, 'estacionamiento_permitido')
        #estacion de ferrocarril
        estacion=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/estacion-de-ferrocarril.gif', 24, 24)
        
        estacion.set_from_pixbuf(pixbuf)
        estacionb=Gtk.Button()
        estacionb.add(estacion)
        estacionb.connect('clicked', self.detalle, conociendo, salir, win, 'estacion_de_ferrocarril')
        #estacion de servicio
        estacion2=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/estacion-de-servicio.gif', 24, 24)
        
        estacion2.set_from_pixbuf(pixbuf)
        estacion2b=Gtk.Button()
        estacion2b.add(estacion2)
        estacion2b.connect('clicked', self.detalle, conociendo, salir, win, 'estacion_de_servicio')
        #fin de autopista
        fina=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/fin-de-autopista.gif', 24, 24)
        
        fina.set_from_pixbuf(pixbuf)
        finab=Gtk.Button()
        finab.add(fina)
        finab.connect('clicked', self.detalle, conociendo, salir, win, 'fin_de_autopista')
        #gomeria
        gomeria=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/gomeria.gif', 24, 24)
        
        gomeria.set_from_pixbuf(pixbuf)
        gomeriab=Gtk.Button()
        gomeriab.add(gomeria)
        gomeriab.connect('clicked', self.detalle, conociendo, salir, win, 'gomeria')
        #hotel
        hotel=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/hotel.gif', 24, 24)
        
        hotel.set_from_pixbuf(pixbuf)
        hotelb=Gtk.Button()
        hotelb.add(hotel)
        hotelb.connect('clicked', self.detalle, conociendo, salir, win, 'hotel')
        #indicadores de utilizacion
        indicadores=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/indicadore-de-utilizacion-d.gif', 24, 24)
        
        indicadores.set_from_pixbuf(pixbuf)
        indicadoresb=Gtk.Button()
        indicadoresb.add(indicadores)
        indicadoresb.connect('clicked', self.detalle, conociendo, salir, win, 'indicadore-de-utilizacion-d')
        #lugar para recreacion y descanso
        recreacion=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/lugar-para-recreacion-y-des.gif', 24, 24)
        
        recreacion.set_from_pixbuf(pixbuf)
        recreacionb=Gtk.Button()
        recreacionb.add(recreacion)
        recreacionb.connect('clicked', self.detalle, conociendo, salir, win, 'lugar-para-recreacion')
        #museo
        museo=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/museo.gif', 24, 24)
        
        museo.set_from_pixbuf(pixbuf)
        museob=Gtk.Button()
        museob.add(museo)
        museob.connect('clicked', self.detalle, conociendo, salir, win, 'museo')
        #parada
        parada=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/parada.gif', 24, 24)
        
        parada.set_from_pixbuf(pixbuf)
        paradab=Gtk.Button()
        paradab.add(parada)
        paradab.connect('clicked', self.detalle, conociendo, salir, win, 'parada')
        #permitido girar derecha
        pgd=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/permitido-girar-derecha.gif', 24, 24)
        
        pgd.set_from_pixbuf(pixbuf)
        pgdb=Gtk.Button()
        pgdb.add(pgd)
        pgdb.connect('clicked', self.detalle, conociendo, salir, win, 'permitido-girar-derecha')
        #permitido girar izquierda
        pgi=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/permitido-girar-izquierda.gif', 24, 24)
        
        pgi.set_from_pixbuf(pixbuf)
        pgib=Gtk.Button()
        pgib.add(pgi)
        pgib.connect('clicked', self.detalle, conociendo, salir, win, 'permitido-girar-izquierda')
        #playa
        playa=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/playa.gif', 24, 24)
        
        playa.set_from_pixbuf(pixbuf)
        playab=Gtk.Button()
        playab.add(playa)
        playab.connect('clicked', self.detalle, conociendo, salir, win, 'playa')
        #plaza
        plaza=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/plaza.gif', 24, 24)
        
        plaza.set_from_pixbuf(pixbuf)
        plazab=Gtk.Button()
        plazab.add(plaza)
        plazab.connect('clicked', self.detalle, conociendo, salir, win, 'plaza')
        #policia
        policia=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/policia.gif', 24, 24)
        
        policia.set_from_pixbuf(pixbuf)
        policiab=Gtk.Button()
        policiab.add(policia)
        policiab.connect('clicked', self.detalle, conociendo, salir, win, 'policia')
        #puesto sanitario
        ps=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/puesto_sanitario.gif', 24, 24)
        
        ps.set_from_pixbuf(pixbuf)
        psb=Gtk.Button()
        psb.add(ps)
        psb.connect('clicked', self.detalle, conociendo, salir, win, 'puesto_sanitario')
        #punto panoramico
        pp=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/punto-panoramico.gif', 24, 24)
        
        pp.set_from_pixbuf(pixbuf)
        ppb=Gtk.Button()
        ppb.add(pp)
        ppb.connect('clicked', self.detalle, conociendo, salir, win, 'punto-panoramico')
        #restaurante
        restaurante=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/restaurante.gif', 24, 24)
        
        restaurante.set_from_pixbuf(pixbuf)
        restauranteb=Gtk.Button()
        restauranteb.add(restaurante)
        restauranteb.connect('clicked', self.detalle, conociendo, salir, win, 'restaurante')
        #servicio mecanico
        mecanico=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/servicio-mecanico.gif', 24, 24)
        
        mecanico.set_from_pixbuf(pixbuf)
        mecanicob=Gtk.Button()
        mecanicob.add(mecanico)
        mecanicob.connect('clicked', self.detalle, conociendo, salir, win, 'servicio-mecanico')
        #servicio telefonico
        telefono=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/servicio-telefonico.gif', 24, 24)
        
        telefono.set_from_pixbuf(pixbuf)
        telefonob=Gtk.Button()
        telefonob.add(telefono)
        telefonob.connect('clicked', self.detalle, conociendo, salir, win, 'servicio-telefonico')
        #taxi
        taxi=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/taxi.gif', 24, 24)
        
        taxi.set_from_pixbuf(pixbuf)
        taxib=Gtk.Button()
        taxib.add(taxi)
        taxib.connect('clicked', self.detalle, conociendo, salir, win, 'taxi')
        #teleferico
        teleferico=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/teleferico.gif', 24, 24)
        
        teleferico.set_from_pixbuf(pixbuf)
        telefericob=Gtk.Button()
        telefericob.add(teleferico)
        telefericob.connect('clicked', self.detalle, conociendo, salir, win, 'teleferico')
        #terminal de omnibus
        terminal=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/terminal-de-omnibus.gif', 24, 24)
        
        terminal.set_from_pixbuf(pixbuf)
        terminalb=Gtk.Button()
        terminalb.add(terminal)
        terminalb.connect('clicked', self.detalle, conociendo, salir, win, 'terminal-de-omnibus')
        #velocidades maximas permitidas
        velocidades=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/informativas/velocidades-maximas-permiti.gif', 24, 24)
        
        velocidades.set_from_pixbuf(pixbuf)
        velocidadesb=Gtk.Button()
        velocidadesb.add(velocidades)
        velocidadesb.connect('clicked', self.detalle, conociendo, salir, win, 'velocidades-maximas-permiti')

        #Desde aqui imagenes preventivas con sus respectivos botones :)
        
        #altura-limitada
        altural=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/altura-limitada.gif', 24, 24)
        
        altural.set_from_pixbuf(pixbuf)
        alturalb=Gtk.Button()
        alturalb.add(altural)
        alturalb.connect('clicked', self.detalle, conociendo, salir, win, 'altura-limitada')
        #ambulancia
        ambulanciaes=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/ambulancia.gif', 24, 24)
        
        ambulanciaes.set_from_pixbuf(pixbuf)
        ambulanciab=Gtk.Button()
        ambulanciab.add(ambulanciaes)
        ambulanciab.connect('clicked', self.detalle, conociendo, salir, win, 'ambulancia')
        #ancho-limitado
        anchol=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/ancho-limitado.gif', 24, 24)
        
        anchol.set_from_pixbuf(pixbuf)
        ancholb=Gtk.Button()
        ancholb.add(anchol)
        ancholb.connect('clicked', self.detalle, conociendo, salir, win, 'ancho-limitado')  
        #animales-sueltos-ciervos
        asc=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/animales-sueltos-ciervos.gif', 24, 24)
        
        asc.set_from_pixbuf(pixbuf)
        ascb=Gtk.Button()
        ascb.add(asc)
        ascb.connect('clicked', self.detalle, conociendo, salir, win, 'animales-sueltos-ciervos')   
        #animales-sueltos-vaca
        asv=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/animales-sueltos-vaca.gif', 24, 24)
        
        asv.set_from_pixbuf(pixbuf)
        asvb=Gtk.Button()
        asvb.add(asv)
        asvb.connect('clicked', self.detalle, conociendo, salir, win, 'animales-sueltos-vaca')  
        #calzada-dividida
        cd=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/calzada-dividida.gif', 24, 24)
        
        cd.set_from_pixbuf(pixbuf)
        cdb=Gtk.Button()
        cdb.add(cd)
        cdb.connect('clicked', self.detalle, conociendo, salir, win, 'calzada-dividida')
        #calzada-rezbaladiza
        cr=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/calzada-rezbaladiza.gif', 24, 24)
        
        cr.set_from_pixbuf(pixbuf)
        crb=Gtk.Button()
        crb.add(cr)
        crb.connect('clicked', self.detalle, conociendo, salir, win, 'calzada-rezbaladiza')
        #Camino sinuoso
        caminos=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Camino-sinuoso.gif', 24, 24)
        
        caminos.set_from_pixbuf(pixbuf)
        caminosb=Gtk.Button()
        caminosb.add(caminos)
        caminosb.connect('clicked', self.detalle, conociendo, salir, win, 'Camino-sinuoso')
        #ciclista
        ciclista=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/ciclista.gif', 24, 24)
        
        ciclista.set_from_pixbuf(pixbuf)
        ciclistab=Gtk.Button()
        ciclistab.add(ciclista)
        ciclistab.connect('clicked', self.detalle, conociendo, salir, win, 'ciclista')
        #corredor-aereo
        corredora=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/corredor-aereo.gif', 24, 24)
        
        corredora.set_from_pixbuf(pixbuf)
        corredorab=Gtk.Button()
        corredorab.add(corredora)
        corredorab.connect('clicked', self.detalle, conociendo, salir, win, 'corredor-aereo')   
        #Curva(comun)
        curvac=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Curva(comun).gif', 24, 24)
        
        curvac.set_from_pixbuf(pixbuf)
        curvacb=Gtk.Button()
        curvacb.add(curvac)
        curvacb.connect('clicked', self.detalle, conociendo, salir, win, 'Curva(comun)')
        #Curva (Contracurva)
        contracurva=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Curva-(Contracurva).gif', 24, 24)
        
        contracurva.set_from_pixbuf(pixbuf)
        contracurvab=Gtk.Button()
        contracurvab.add(contracurva)
        contracurvab.connect('clicked', self.detalle, conociendo, salir, win, 'Curva(Contracurva)') 
        #Curva-en-S
        curvaens=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Curva-en-S.gif', 24, 24)
        
        curvaens.set_from_pixbuf(pixbuf)
        curvaensb=Gtk.Button()
        curvaensb.add(curvaens)
        curvaensb.connect('clicked', self.detalle, conociendo, salir, win, 'Curva-en-S')    


        #derrumbes
        derrumbes=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/derrumbes.gif', 24, 24)
        
        derrumbes.set_from_pixbuf(pixbuf)
        derrumbesb=Gtk.Button()
        derrumbesb.add(derrumbes)
        derrumbesb.connect('clicked', self.detalle, conociendo, salir, win, 'derrumbes')
        #encricijada-bifurcacion
        enbi=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/encricijada-bifurcacion.gif', 24, 24)
        
        enbi.set_from_pixbuf(pixbuf)
        enbib=Gtk.Button()
        enbib.add(enbi)
        enbib.connect('clicked', self.detalle, conociendo, salir, win, 'encricijada-bifurcacion')   
        #encricijada-bifurcacion2
        enbi2=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/encricijada-bifurcacion2.gif', 24, 24)
        
        enbi2.set_from_pixbuf(pixbuf)
        enbi2b=Gtk.Button()
        enbi2b.add(enbi2)
        enbi2b.connect('clicked', self.detalle, conociendo, salir, win, 'encricijada-bifurcacion2') 
        #encricijada-empalme
        enem=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/encricijada-empalme.gif', 24, 24)
        
        enem.set_from_pixbuf(pixbuf)
        enemb=Gtk.Button()
        enemb.add(enem)
        enemb.connect('clicked', self.detalle, conociendo, salir, win, 'encricijada-empalme')
        #encrucijada-cruce
        encr=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/encrucijada-cruce.gif', 24, 24)
        
        encr.set_from_pixbuf(pixbuf)
        encrb=Gtk.Button()
        encrb.add(encr)
        encrb.connect('clicked', self.detalle, conociendo, salir, win, 'encrucijada-cruce') 
        #escolares
        escolares=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/escolares.gif', 24, 24)
        
        escolares.set_from_pixbuf(pixbuf)
        escolaresb=Gtk.Button()
        escolaresb.add(escolares)
        escolaresb.connect('clicked', self.detalle, conociendo, salir, win, 'escolares')    
        #Estrechamiento (una sola mano)
        estrechamientom=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Estrechamient(unasolamano).gif', 24, 24)
        
        estrechamientom.set_from_pixbuf(pixbuf)
        estrechamientomb=Gtk.Button()
        estrechamientomb.add(estrechamientom)
        estrechamientomb.connect('clicked', self.detalle, conociendo, salir, win, 'Estrechamient(unasolamano)') 
        #Estrechamiento(dosmanos)
        estrecho=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Etrechamiento(dosmanos).gif', 24, 24)
        
        estrecho.set_from_pixbuf(pixbuf)
        estrechob=Gtk.Button()
        estrechob.add(estrecho)
        estrechob.connect('clicked', self.detalle, conociendo, salir, win, 'Etrechamiento(dosmanos)')   
        #flecha-direccional
        flechad=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/flecha-direccional.gif', 24, 24)
        
        flechad.set_from_pixbuf(pixbuf)
        flechadb=Gtk.Button()
        flechadb.add(flechad)
        flechadb.connect('clicked', self.detalle, conociendo, salir, win, 'flecha-direccional') 
        #flecha-direccional2
        flechad2=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/flecha-direccional2.gif', 24, 24)
        
        flechad2.set_from_pixbuf(pixbuf)
        flechad2b=Gtk.Button()
        flechad2b.add(flechad2)
        flechad2b.connect('clicked', self.detalle, conociendo, salir, win, 'flecha-direccional2')   
        #incorporacion-de-transito-l
        incor=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/incorporacion-de-transito-l.gif', 24, 24)
        
        incor.set_from_pixbuf(pixbuf)
        incorb=Gtk.Button()
        incorb.add(incor)
        incorb.connect('clicked', self.detalle, conociendo, salir, win, 'incorporacion-de-transito-l')  
        #inicio-de-doble-circulacion
        iniciodoble=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/inicio-de-doble-circulacion.gif', 24, 24)
        
        iniciodoble.set_from_pixbuf(pixbuf)
        iniciodobleb=Gtk.Button()
        iniciodobleb.add(iniciodoble)
        iniciodobleb.connect('clicked', self.detalle, conociendo, salir, win, 'inicio-de-doble-circulacion')    
        #jinete
        jinete=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/jinete.gif', 24, 24)
        
        jinete.set_from_pixbuf(pixbuf)
        jineteb=Gtk.Button()
        jineteb.add(jinete)
        jineteb.connect('clicked', self.detalle, conociendo, salir, win, 'jinete')  
        #Ninos
        Ninos=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Ninos.gif', 24, 24)
        
        Ninos.set_from_pixbuf(pixbuf)
        Ninosb=Gtk.Button()
        Ninosb.add(Ninos)
        Ninosb.connect('clicked', self.detalle, conociendo, salir, win, 'Ninos')    
        #paso
        paso=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/paso.gif', 24, 24)
        
        paso.set_from_pixbuf(pixbuf)
        pasob=Gtk.Button()
        pasob.add(paso)
        pasob.connect('clicked', self.detalle, conociendo, salir, win, 'paso')  
        #Pendiente(ascendente)
        pendienteas=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Pendiente(ascendente).gif', 24, 24)
        
        pendienteas.set_from_pixbuf(pixbuf)
        pendienteasb=Gtk.Button()
        pendienteasb.add(pendienteas)
        pendienteasb.connect('clicked', self.detalle, conociendo, salir, win, 'Pendiente(ascendente)')  
        #Pendiente(descendente)
        pendientedes=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Pendienteabajo.gif', 24, 24)
        
        pendientedes.set_from_pixbuf(pixbuf)
        pendientedesb=Gtk.Button()
        pendientedesb.add(pendientedes)
        pendientedesb.connect('clicked', self.detalle, conociendo, salir, win, 'Pendienteabajo')    
        #Perfil(Irregular)
        perfilirre=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Perfilirregular.gif', 24, 24)
        
        perfilirre.set_from_pixbuf(pixbuf)
        perfilirreb=Gtk.Button()
        perfilirreb.add(perfilirre)
        perfilirreb.connect('clicked', self.detalle, conociendo, salir, win, 'Perfilirregular') 
        #Perfil(Irregular2)
        perfilirre2=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/perfilirregular2.gif', 24, 24)
        
        perfilirre2.set_from_pixbuf(pixbuf)
        perfilirre2b=Gtk.Button()
        perfilirre2b.add(perfilirre2)
        perfilirre2b.connect('clicked', self.detalle, conociendo, salir, win, 'perfilirregular2')   
        #perfil-irregular-lomada
        perfilirre3=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/perfil-irregular-lomada.gif', 24, 24)
        
        perfilirre3.set_from_pixbuf(pixbuf)
        perfilirre3b=Gtk.Button()
        perfilirre3b.add(perfilirre3)
        perfilirre3b.connect('clicked', self.detalle, conociendo, salir, win, 'perfil-irregular-lomada')    
        #presencia-de-tranvia
        presencia=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/presencia-de-tranvia.gif', 24, 24)
        
        presencia.set_from_pixbuf(pixbuf)
        presenciab=Gtk.Button()
        presenciab.add(presencia)
        presenciab.connect('clicked', self.detalle, conociendo, salir, win, 'presencia-de-tranvia') 

        
        #proximidad-de-pare
        proximidadpare=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/proximidad-de-pare.gif', 24, 24)
        
        proximidadpare.set_from_pixbuf(pixbuf)
        proximidadpareb=Gtk.Button()
        proximidadpareb.add(proximidadpare)
        proximidadpareb.connect('clicked', self.detalle, conociendo, salir, win, 'proximidad-de-pare')  
        #proximidad-restrictiva
        prestrictiva=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/proximidad-restrictiva.gif', 24, 24)
        
        prestrictiva.set_from_pixbuf(pixbuf)
        prestrictivab=Gtk.Button()
        prestrictivab.add(prestrictiva)
        prestrictivab.connect('clicked', self.detalle, conociendo, salir, win, 'proximidad-restrictiva')    
        #proyeccion-de-piedras
        proyeccion=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/proyeccion-de-piedras.gif', 24, 24)
        
        proyeccion.set_from_pixbuf(pixbuf)
        proyeccionb=Gtk.Button()
        proyeccionb.add(proyeccion)
        proyeccionb.connect('clicked', self.detalle, conociendo, salir, win, 'proyeccion-de-piedras')   
        #puente-angosto
        puenteangosto=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/puente-angosto.gif', 24, 24)
        
        puenteangosto.set_from_pixbuf(pixbuf)
        puenteangostob=Gtk.Button()
        puenteangostob.add(puenteangosto)
        puenteangostob.connect('clicked', self.detalle, conociendo, salir, win, 'puente-angosto')   
        #puente-movil
        puentemovil=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/puente-movil.gif', 24, 24)
        
        puentemovil.set_from_pixbuf(pixbuf)
        puentemovilb=Gtk.Button()
        puentemovilb.add(puentemovil)
        puentemovilb.connect('clicked', self.detalle, conociendo, salir, win, 'puente-movil')   
        #rotonda
        rotonda=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/rotonda.gif', 24, 24)
        
        rotonda.set_from_pixbuf(pixbuf)
        rotondab=Gtk.Button()
        rotondab.add(rotonda)
        rotondab.connect('clicked', self.detalle, conociendo, salir, win, 'rotonda')    
        #semaforo
        semaforoo=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/semaforo.gif', 24, 24)
        
        semaforoo.set_from_pixbuf(pixbuf)
        semaforoob=Gtk.Button()
        semaforoob.add(semaforoo)
        semaforoob.connect('clicked', self.detalle, conociendo, salir, win, 'semaforo') 
        #tractor
        tractor=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/tractor.gif', 24, 24)
        
        tractor.set_from_pixbuf(pixbuf)
        tractorb=Gtk.Button()
        tractorb.add(tractor)
        tractorb.connect('clicked', self.detalle, conociendo, salir, win, 'tractor')    
        #tunel
        tunel=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/tunel.gif', 24, 24)
        
        tunel.set_from_pixbuf(pixbuf)
        tunelb=Gtk.Button()
        tunelb.add(tunel)
        tunelb.connect('clicked', self.detalle, conociendo, salir, win, 'tunel')    
        #vientos-fuertes-laterales
        vientosfuertes=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/vientos-fuertes-laterales.gif', 24, 24)
        
        vientosfuertes.set_from_pixbuf(pixbuf)
        vientosfuertesb=Gtk.Button()
        vientosfuertesb.add(vientosfuertes)
        vientosfuertesb.connect('clicked', self.detalle, conociendo, salir, win, 'vientos-fuertes-laterales')   
        
        #Reglamentarias Imagenes y botones

        #circulacion_exclusiva_peatones
        circulacion_exlusiva_peatonesb=Gtk.Button() 
        circulacion_exlusiva_peatones=Gtk.Image()
        reglamentariasV2.add(circulacion_exlusiva_peatonesb)
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/circulacion_exlusiva_peatones.png', 24, 24)
        
        circulacion_exlusiva_peatones.set_from_pixbuf(pixbuf)
        circulacion_exlusiva_peatonesb.add(circulacion_exlusiva_peatones)
        circulacion_exlusiva_peatonesb.connect('clicked', self.detalle, conociendo, salir, win, 'circulacion_exlusiva_peatones')
        #circulaion_exlusica_bicicletas
        circulaion_exlusica_bicicletas=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/circulaion_exlusica_bicicletas.png', 24, 24)
        
        circulaion_exlusica_bicicletas.set_from_pixbuf(pixbuf)
        circulaion_exlusica_bicicletasb=Gtk.Button()
        circulaion_exlusica_bicicletasb.add(circulaion_exlusica_bicicletas)
        reglamentariasV2.add(circulaion_exlusica_bicicletasb)
        circulaion_exlusica_bicicletasb.connect('clicked', self.detalle, conociendo, salir, win, 'circulaion_exlusica_bicicletas')

            #circulaion_exlusica_jinetes
        circulaion_exlusica_jinetes=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/circulaion_exlusica_jinetes.png', 24, 24)
        
        circulaion_exlusica_jinetes.set_from_pixbuf(pixbuf)
        circulaion_exlusica_jinetesb=Gtk.Button()
        circulaion_exlusica_jinetesb.add(circulaion_exlusica_jinetes)
        reglamentariasV2.add(circulaion_exlusica_jinetesb)
        circulaion_exlusica_jinetesb.connect('clicked', self.detalle, conociendo, salir, win, 'circulaion_exlusica_jinetes')

        #circulaion_exlusica_trans.publico
        circulaion_exlusica_transpublico=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/circula_colectivo.png', 24, 24)
        
        circulaion_exlusica_transpublico.set_from_pixbuf(pixbuf)
        circulaion_exlusica_transpublicob=Gtk.Button()
        circulaion_exlusica_transpublicob.add(circulaion_exlusica_transpublico)
        reglamentariasV2.add(circulaion_exlusica_transpublicob)
        circulaion_exlusica_transpublicob.connect('clicked', self.detalle, conociendo, salir, win, 'circula_colectivo')
        #circulaion_exlusiva_motos
        circulaion_exlusiva_motos=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/circulaion_exlusiva_motos.png', 24, 24)
        
        circulaion_exlusiva_motos.set_from_pixbuf(pixbuf)
        circulaion_exlusiva_motosb=Gtk.Button()
        circulaion_exlusiva_motosb.add(circulaion_exlusiva_motos)
        reglamentariasV2.add(circulaion_exlusiva_motosb)
        circulaion_exlusiva_motosb.connect('clicked', self.detalle, conociendo, salir, win, 'circulaion_exlusiva_motos')
        #contramano
        contramano=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/contramano.png', 24, 24)
        
        contramano.set_from_pixbuf(pixbuf)
        contramanob=Gtk.Button()
        contramanob.add(contramano)
        reglamentariasV2.add(contramanob)
        contramanob.connect('clicked', self.detalle, conociendo, salir, win, 'contramano')
        #estacionamiento_exclusivo
        estacionamiento_exclusivo=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/estacionamiento_exclusivo.png', 24, 24)
        
        estacionamiento_exclusivo.set_from_pixbuf(pixbuf)
        estacionamiento_exclusivob=Gtk.Button()
        estacionamiento_exclusivob.add(estacionamiento_exclusivo)
        reglamentariasV2.add(estacionamiento_exclusivob)
        estacionamiento_exclusivob.connect('clicked', self.detalle, conociendo, salir, win, 'estacionamiento_exclusivo')
        #limitacion_de_altura
        limitacion_de_altura=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/limitacion_de_altura.png', 24, 24)
        
        limitacion_de_altura.set_from_pixbuf(pixbuf)
        limitacion_de_alturab=Gtk.Button()
        limitacion_de_alturab.add(limitacion_de_altura)
        reglamentariasV2.add(limitacion_de_alturab)
        limitacion_de_alturab.connect('clicked', self.detalle, conociendo, salir, win, 'limitacion_de_altura')
        #limitacion_de_ancho
        limitacion_de_ancho=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/limitacion_de_ancho.png', 24, 24)
        
        limitacion_de_ancho.set_from_pixbuf(pixbuf)
        limitacion_de_anchob=Gtk.Button()
        limitacion_de_anchob.add(limitacion_de_ancho)
        reglamentariasV2.add(limitacion_de_anchob)
        limitacion_de_anchob.connect('clicked', self.detalle, conociendo, salir, win, 'limitacion_de_ancho')
        #limitacion_de_largo_de_vehiculo
        limitacion_de_largo_de_vehiculo=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/limitacion_de_largo_de_vehiculo.png', 24, 24)
        
        limitacion_de_largo_de_vehiculo.set_from_pixbuf(pixbuf)
        limitacion_de_largo_de_vehiculob=Gtk.Button()
        limitacion_de_largo_de_vehiculob.add(limitacion_de_largo_de_vehiculo)
        reglamentariasV2.add(limitacion_de_largo_de_vehiculob)
        limitacion_de_largo_de_vehiculob.connect('clicked', self.detalle, conociendo, salir, win, 'limitacion_de_largo_de_vehiculo')
        #limitacion_de_peso
        limitacion_de_peso=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/limitacion_de_peso.png', 24, 24)
        
        limitacion_de_peso.set_from_pixbuf(pixbuf)
        limitacion_de_pesob=Gtk.Button()
        limitacion_de_pesob.add(limitacion_de_peso)
        reglamentariasV2.add(limitacion_de_pesob)
        limitacion_de_pesob.connect('clicked', self.detalle, conociendo, salir, win, 'limitacion_de_peso')

        #limitacion_de_peso_2
        limitacion_de_peso_2=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/limitacion_de_peso_2.png', 24, 24)
        
        limitacion_de_peso_2.set_from_pixbuf(pixbuf)
        limitacion_de_peso_2b=Gtk.Button()
        limitacion_de_peso_2b.add(limitacion_de_peso_2)
        reglamentariasV3.add(limitacion_de_peso_2b)
        limitacion_de_peso_2b.connect('clicked', self.detalle, conociendo, salir, win, 'limitacion_de_peso_2')
        #limite_de_velocidad_maxima
        limite_de_velocidad_maxima=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/limite_de_velocidad_maxima.png', 24, 24)
        
        limite_de_velocidad_maxima.set_from_pixbuf(pixbuf)
        limite_de_velocidad_maximab=Gtk.Button()
        limite_de_velocidad_maximab.add(limite_de_velocidad_maxima)
        reglamentariasV3.add(limite_de_velocidad_maximab)
        limite_de_velocidad_maximab.connect('clicked', self.detalle, conociendo, salir, win, 'limite_de_velocidad_maxima')
        #limite_de_velocidad_minima
        limite_de_velocidad_minima=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/limite_de_velocidad_minima.png', 24, 24)
        
        limite_de_velocidad_minima.set_from_pixbuf(pixbuf)
        limite_de_velocidad_minimab=Gtk.Button()
        limite_de_velocidad_minimab.add(limite_de_velocidad_minima)
        reglamentariasV3.add(limite_de_velocidad_minimab)
        limite_de_velocidad_minimab.connect('clicked', self.detalle, conociendo, salir, win, 'limite_de_velocidad_minima')
        #no_avanzar
        no_avanzar=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/no_avanzar.png', 24, 24)
        
        no_avanzar.set_from_pixbuf(pixbuf)
        no_avanzarb=Gtk.Button()
        no_avanzarb.add(no_avanzar)
        reglamentariasV3.add(no_avanzarb)
        no_avanzarb.connect('clicked', self.detalle, conociendo, salir, win, 'no_avanzar')
        #no_estacionar
        no_estacionar=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/no_estacionar.png', 24, 24)
        
        no_estacionar.set_from_pixbuf(pixbuf)
        no_estacionarb=Gtk.Button()
        no_estacionarb.add(no_estacionar)
        reglamentariasV3.add(no_estacionarb)
        no_estacionarb.connect('clicked', self.detalle, conociendo, salir, win, 'no_estacionar')
        #no_estacionar_ni_detenerse
        no_estacionar_ni_detenerse=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/no_estacionar_ni_detenerse.png', 24, 24)
        
        no_estacionar_ni_detenerse.set_from_pixbuf(pixbuf)
        no_estacionar_ni_detenerseb=Gtk.Button()
        no_estacionar_ni_detenerseb.add(no_estacionar_ni_detenerse)
        reglamentariasV3.add(no_estacionar_ni_detenerseb)
        no_estacionar_ni_detenerseb.connect('clicked', self.detalle, conociendo, salir, win, 'no_estacionar_ni_detenerse')

        #no_girar_a_la_derecha
        no_girar_a_la_derecha=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/no_girar_a_la_derecha.png', 24, 24)
        
        no_girar_a_la_derecha.set_from_pixbuf(pixbuf)
        no_girar_a_la_derechab=Gtk.Button()
        no_girar_a_la_derechab.add(no_girar_a_la_derecha)
        reglamentariasV3.add(no_girar_a_la_derechab)
        no_girar_a_la_derechab.connect('clicked', self.detalle, conociendo, salir, win, 'no_girar_a_la_derecha')
        #no_girar_a_la_izquierda
        no_girar_a_la_izquierda=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/no_girar_a_la_izquierda.png', 24, 24)
        
        no_girar_a_la_izquierda.set_from_pixbuf(pixbuf)
        no_girar_a_la_izquierdab=Gtk.Button()
        no_girar_a_la_izquierdab.add(no_girar_a_la_izquierda)
        reglamentariasV3.add(no_girar_a_la_izquierdab)
        no_girar_a_la_izquierdab.connect('clicked', self.detalle, conociendo, salir, win, 'no_girar_a_la_izquierda')
        #no_girar_en_u
        no_girar_en_u=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/no_girar_en_u.png', 24, 24)
        
        no_girar_en_u.set_from_pixbuf(pixbuf)
        no_girar_en_ub=Gtk.Button()
        no_girar_en_ub.add(no_girar_en_u)
        reglamentariasV3.add(no_girar_en_ub)
        no_girar_en_ub.connect('clicked', self.detalle, conociendo, salir, win, 'no_girar_en_u')
        #no_ruido_molesto
        no_ruido_molesto=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/no_ruido_molesto.png', 24, 24)
        
        no_ruido_molesto.set_from_pixbuf(pixbuf)
        no_ruido_molestob=Gtk.Button()
        no_ruido_molestob.add(no_ruido_molesto)
        reglamentariasV3.add(no_ruido_molestob)
        no_ruido_molestob.connect('clicked', self.detalle, conociendo, salir, win, 'no_ruido_molesto')
        #prohibicion_de_cambiar_de_carril
        prohibicion_de_cambiar_de_carril=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/prohibicion_de_cambiar_de_carril.png', 24, 24)
        
        prohibicion_de_cambiar_de_carril.set_from_pixbuf(pixbuf)
        prohibicion_de_cambiar_de_carrilb=Gtk.Button()
        prohibicion_de_cambiar_de_carrilb.add(prohibicion_de_cambiar_de_carril)
        reglamentariasV3.add(prohibicion_de_cambiar_de_carrilb)
        prohibicion_de_cambiar_de_carrilb.connect('clicked', self.detalle, conociendo, salir, win, 'prohibicion_de_cambiar_de_carril')
        #prohibicion_de_circular_acoplado
        prohibicion_de_circular_acoplado=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/prohibicion_de_circular_acoplado.png', 24, 24)
        
        prohibicion_de_circular_acoplado.set_from_pixbuf(pixbuf)
        prohibicion_de_circular_acopladob=Gtk.Button()
        prohibicion_de_circular_acopladob.add(prohibicion_de_circular_acoplado)
        reglamentariasV4.add(prohibicion_de_circular_acopladob)
        prohibicion_de_circular_acopladob.connect('clicked', self.detalle, conociendo, salir, win, 'prohibicion_de_circular_acoplado')
        #prohibicion_de_circular_animal
        prohibicion_de_circular_animal=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/prohibicion_de_circular_animal.png', 24, 24)
        
        prohibicion_de_circular_animal.set_from_pixbuf(pixbuf)
        prohibicion_de_circular_animalb=Gtk.Button()
        prohibicion_de_circular_animalb.add(prohibicion_de_circular_animal)
        reglamentariasV4.add(prohibicion_de_circular_animalb)
        prohibicion_de_circular_animalb.connect('clicked', self.detalle, conociendo, salir, win, 'prohibicion_de_circular_animal')
        #prohibicion_de_circular_autos
        prohibicion_de_circular_autos=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/prohibicion_de_circular_autos.png', 24, 24)
        
        prohibicion_de_circular_autos.set_from_pixbuf(pixbuf)
        prohibicion_de_circular_autosb=Gtk.Button()
        prohibicion_de_circular_autosb.add(prohibicion_de_circular_autos)
        reglamentariasV4.add(prohibicion_de_circular_autosb)
        prohibicion_de_circular_autosb.connect('clicked', self.detalle, conociendo, salir, win, 'prohibicion_de_circular_autos')
        #prohibicion_de_circular_bicibletas
        prohibicion_de_circular_bicibletas=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/prohibicion_de_circular_bicibletas.png', 24, 24)
        
        prohibicion_de_circular_bicibletas.set_from_pixbuf(pixbuf)
        prohibicion_de_circular_bicibletasb=Gtk.Button()
        prohibicion_de_circular_bicibletasb.add(prohibicion_de_circular_bicibletas)
        reglamentariasV4.add(prohibicion_de_circular_bicibletasb)
        prohibicion_de_circular_bicibletasb.connect('clicked', self.detalle, conociendo, salir, win, 'prohibicion_de_circular_bicibletas')
        #prohibicion_de_circular_camion
        prohibicion_de_circular_camion=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/prohibicion_de_circular_camion.png', 24, 24)
        
        prohibicion_de_circular_camion.set_from_pixbuf(pixbuf)
        prohibicion_de_circular_camionb=Gtk.Button()
        prohibicion_de_circular_camionb.add(prohibicion_de_circular_camion)
        reglamentariasV4.add(prohibicion_de_circular_camionb)
        prohibicion_de_circular_camionb.connect('clicked', self.detalle, conociendo, salir, win, 'prohibicion_de_circular_camion')
        #prohibicion_de_circular_carro_mano
        prohibicion_de_circular_carro_mano=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/prohibicion_de_circular_carro_mano.png', 24, 24)
        
        prohibicion_de_circular_carro_mano.set_from_pixbuf(pixbuf)
        prohibicion_de_circular_carro_manob=Gtk.Button()
        prohibicion_de_circular_carro_manob.add(prohibicion_de_circular_carro_mano)
        reglamentariasV4.add(prohibicion_de_circular_carro_manob)
        prohibicion_de_circular_carro_manob.connect('clicked', self.detalle, conociendo, salir, win, 'prohibicion_de_circular_carro_mano')
        #prohibicion_de_circular_motos
        prohibicion_de_circular_motos=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/prohibicion_de_circular_motos.png', 24, 24)
        
        prohibicion_de_circular_motos.set_from_pixbuf(pixbuf)
        prohibicion_de_circular_motosb=Gtk.Button()
        prohibicion_de_circular_motosb.add(prohibicion_de_circular_motos)
        reglamentariasV4.add(prohibicion_de_circular_motosb)
        prohibicion_de_circular_motosb.connect('clicked', self.detalle, conociendo, salir, win, 'prohibicion_de_circular_motos')
        #prohibicion_de_circular_peaton
        prohibicion_de_circular_peaton=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/prohibicion_de_circular_peaton.png', 24, 24)
        
        prohibicion_de_circular_peaton.set_from_pixbuf(pixbuf)
        prohibicion_de_circular_peatonb=Gtk.Button()
        prohibicion_de_circular_peatonb.add(prohibicion_de_circular_peaton)
        reglamentariasV4.add(prohibicion_de_circular_peatonb)
        prohibicion_de_circular_peatonb.connect('clicked', self.detalle, conociendo, salir, win, 'prohibicion_de_circular_peaton')
        #prohibicion_de_circular_trac.an
        prohibicion_de_circular_tracan=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/prohibicion_de_circular_trac.an.png', 24, 24)
        
        prohibicion_de_circular_tracan.set_from_pixbuf(pixbuf)
        prohibicion_de_circular_tracanb=Gtk.Button()
        prohibicion_de_circular_tracanb.add(prohibicion_de_circular_tracan)
        reglamentariasV4.add(prohibicion_de_circular_tracanb)
        prohibicion_de_circular_tracanb.connect('clicked', self.detalle, conociendo, salir, win, 'prohibicion_de_circular_trac.an')
        #prohibicion_de_circular_tractor
        prohibicion_de_circular_tractor=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/prohibicion_de_circular_tractor.png', 24, 24)
        
        prohibicion_de_circular_tractor.set_from_pixbuf(pixbuf)
        prohibicion_de_circular_tractorb=Gtk.Button()
        prohibicion_de_circular_tractorb.add(prohibicion_de_circular_tractor)
        reglamentariasV4.add(prohibicion_de_circular_tractorb)
        prohibicion_de_circular_tractorb.connect('clicked', self.detalle, conociendo, salir, win, 'prohibicion_de_circular_tractor')
        #prohibido_adelantar
        prohibido_adelantar=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/prohibido_adelantar.png', 24, 24)
        
        prohibido_adelantar.set_from_pixbuf(pixbuf)
        prohibido_adelantarb=Gtk.Button()
        prohibido_adelantarb.add(prohibido_adelantar)
        reglamentariasV4.add(prohibido_adelantarb)
        prohibido_adelantarb.connect('clicked', self.detalle, conociendo, salir, win, 'prohibido_adelantar')
        #Atencion
        Atencion = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Atencion.png', 24, 24)
        
        Atencion.set_from_pixbuf(pixbuf)
        Atencionb=Gtk.Button()
        Atencionb.add(Atencion)
        preventivasimg2.add(Atencionb)
        Atencionb.connect('clicked', self.detalle, conociendo, salir, win, 'Atencion')
            #Cruce de_Peatoes
        Cruce_de_Peatoes=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Cruce_de_Peatoes.png', 24, 24)
        
        Cruce_de_Peatoes.set_from_pixbuf(pixbuf)
        Cruce_de_Peatoesb=Gtk.Button()
        Cruce_de_Peatoesb.add(Cruce_de_Peatoes)
        preventivasimg2.add(Cruce_de_Peatoesb)
        Cruce_de_Peatoesb.connect('clicked', self.detalle, conociendo, salir, win, 'Cruce_de_Peatoes')
             #Cruce_ferrioviario
        Cruce_ferrioviario=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Cruce_ferrioviario.png', 24, 24)
        
        Cruce_ferrioviario.set_from_pixbuf(pixbuf)
        Cruce_ferrioviariob=Gtk.Button()
        Cruce_ferrioviariob.add(Cruce_ferrioviario)
        preventivasimg2.add(Cruce_ferrioviariob)
        Cruce_ferrioviariob.connect('clicked', self.detalle, conociendo, salir, win, 'Cruce_ferrioviario')
            #Curva_Cerrada
        Curva_Cerrada=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Curva_Cerrada.png', 24, 24)
        
        Curva_Cerrada.set_from_pixbuf(pixbuf)
        Curva_Cerradab=Gtk.Button()
        Curva_Cerradab.add(Curva_Cerrada)
        preventivasimg2.add(Curva_Cerradab)
        Curva_Cerradab.connect('clicked', self.detalle, conociendo, salir, win, 'Curva_Cerrada')
            #Cuz_de_San_Andres
        Cuz_de_San_Andres=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/preventivas/Cuz_de_San_Andres.png', 24, 24)
        
        Cuz_de_San_Andres.set_from_pixbuf(pixbuf)
        Cuz_de_San_Andresb=Gtk.Button()
        Cuz_de_San_Andresb.add(Cuz_de_San_Andres)
        preventivasimg2.add(Cuz_de_San_Andresb)
        Cuz_de_San_Andresb.connect('clicked', self.detalle, conociendo, salir, win, 'Cuz_de_San_Andres')


        #
        #=Gtk.Image()
        #pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('images/reglamentarias/.png', 24, 24)
        #
            #.set_from_pixbuf(pixbuf)
        #=Gtk.Button()
        ##.add()
        #reglamentariasV3.add()


        #Add's
        #Informativas
        infomage.add(infomage1)
        infomage1.add(aeropuertob)
        infomage1.add(cssb)
        infomage1.add(balneariob)
        infomage1.add(barb)
        infomage1.add(css2b)
        infomage1.add(ptb)
        infomage1.add(campamentob)
        infomage1.add(cdab)
        infomage1.add(correob)
        infomage1.add(dcsb)
        infomage1.add(dp1b)
        infomage1.add(dp2b)
        infomage1.add(dp3b)
        infomage1.add(dp4b)
        infomage1.add(dp5b)
        infomage.add(infomage2) 
        infomage2.add(dp6b)
        infomage2.add(edrb)
        infomage2.add(estacionamientob)
        infomage2.add(estacionamiento2b)
        infomage2.add(estacionamiento3b)
        infomage2.add(estacionb)
        infomage2.add(estacion2b)
        infomage2.add(finab)
        infomage2.add(gomeriab)
        infomage2.add(hotelb)
        infomage2.add(indicadoresb)
        infomage2.add(recreacionb)
        infomage2.add(museob)
        infomage2.add(paradab)
        infomage2.add(pt2b)
        infomage.add(infomage3)
        infomage3.add(pgdb)
        infomage3.add(pgib)
        infomage3.add(playab)
        infomage3.add(plazab)
        infomage3.add(policiab)
        infomage3.add(psb)
        infomage3.add(ppb)
        infomage3.add(restauranteb)
        infomage3.add(mecanicob)
        infomage3.add(telefonob)
        infomage3.add(taxib)
        infomage3.add(telefericob)
        infomage3.add(terminalb)
        infomage3.add(velocidadesb)
        infomage3.add(b)
        #Preventivas
        preventivasimg.add(preventivasimg1)
        preventivasimg1.add(alturalb)
        preventivasimg1.add(ambulanciab)
        preventivasimg1.add(ancholb)
        preventivasimg1.add(ascb)
        preventivasimg1.add(asvb)
        preventivasimg1.add(cdb)
        preventivasimg1.add(crb)
        preventivasimg1.add(caminosb)
        preventivasimg1.add(ciclistab)
        preventivasimg1.add(corredorab)
        preventivasimg1.add(contracurvab)
        preventivasimg1.add(curvaensb)
        preventivasimg1.add(derrumbesb)
        preventivasimg1.add(enbib)
        preventivasimg1.add(vientosfuertesb)
        preventivasimg1.add(pasob)
        preventivasimg1.add(incorb)
        preventivasimg3.add(curvacb)
        preventivasimg.add(preventivasimg2) 
        preventivasimg2.add(enbi2b)
        preventivasimg2.add(enemb)
        preventivasimg2.add(encrb)
        preventivasimg2.add(escolaresb)
        preventivasimg2.add(estrechamientomb)
        preventivasimg2.add(estrechob)
        preventivasimg2.add(flechadb)
        preventivasimg2.add(flechad2b)
        preventivasimg2.add(jineteb)
        preventivasimg2.add(pendienteasb)
        preventivasimg2.add(pendientedesb)
        preventivasimg2.add(h)
        preventivasimg.add(preventivasimg3)
        preventivasimg3.add(perfilirreb)
        preventivasimg3.add(perfilirre2b)
        preventivasimg3.add(perfilirre3b)
        preventivasimg3.add(presenciab)
        preventivasimg3.add(proximidadpareb)
        preventivasimg3.add(prestrictivab)
        preventivasimg3.add(puenteangostob)
        preventivasimg3.add(puentemovilb)
        preventivasimg3.add(rotondab)
        preventivasimg3.add(Ninosb) 
        preventivasimg3.add(proyeccionb)              
        preventivasimg3.add(semaforoob)
        preventivasimg3.add(tractorb)
        preventivasimg3.add(tunelb)
        preventivasimg3.add(iniciodobleb)
        preventivasimg3.add(g)
        conociendo.add(bbox)
        bbox.add(salir)
        bbox.show_all()
        conociendo.show_all()

    def detalle(self, boton, conociendo, salir, win, data):
        for conociendo in win.get_children(): win.remove(conociendo)
        self.windows = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        self.windows.connect("delete-event", Gtk.main_quit)  	

        parser=SafeConfigParser()
        parser.read('Config.ini')
        detalle = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        titulo = Gtk.Label(parser.get(data,'titulo'))
        imagesenal = Gtk.Image()
        info = Gtk.TextView()
        info.set_wrap_mode(Gtk.WrapMode.WORD)
        info.set_editable(False)
        textbuffer = info.get_buffer()
        textbuffer.set_text(parser.get(data,'info'))
        quit = Gtk.Button('Salir')
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(parser.get(data,'image'), 400, 400)
        imagesenal.set_from_pixbuf(pixbuf)
        quit.connect('clicked',self.volver, detalle, conociendo)

        win.add(detalle)
        detalle.add(titulo)
        detalle.add(imagesenal) 
        detalle.add(info)
        detalle.add(quit)
        win.show_all()
    
    def volver(self,win,detalle,conociendo):
    	for detalle in win.get_children(): win.remove(detalle)
       	win.add(conociendo)
        win.show_all()
    def exit(self,win,vbox,menu):
        for vbox in win.get_children(): win.remove(vbox)
        win.add(menu)
        win.show_all()
    def salir1(self,win,menu,historia):	
        for historia in win.get_children(): win.remove(historia)        
        win.add(menu)
       	win.show_all()
    def futurista(self,menu,win,ram,conociendo):
        win.remove(menu)
        self.windows = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        self.windows.connect("delete-event", Gtk.main_quit)
        parser=SafeConfigParser()
        parser.read('Config.ini')
        historia = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        win.add(historia)
        title = Gtk.Label(parser.get('historia' + str (ram),'title'))

        imagehistory = Gtk.Image()
        infohistory = Gtk.TextView()
        infohistory.set_wrap_mode(Gtk.WrapMode.WORD)
        infohistory.set_editable(False)
        textbuffer = infohistory.get_buffer()
        textbuffer.set_text(parser.get('historia' + str (ram),'h'))
        quiti = Gtk.Button('Salir')
        win.show_all()
        historia.add(title) 
        historia.add(imagehistory)
        historia.add(infohistory)
        historia.add(quiti)

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(parser.get('historia' + str (ram),'image'), 400, 400)
        imagehistory.set_from_pixbuf(pixbuf)
        
        historia.show_all()
        quiti.connect('clicked',self.salir1,menu,historia,)
       
    def salir(self, salir, menu, win, conociendo):
    	win.remove(conociendo)
        win.add(menu)
        win.show_all()
        
    def initi(self, sabes,win,menu):
        for menu in win.get_children(): win.remove(menu)
        image = Gtk.Image()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        win.add(vbox)
        button_0 = Gtk.Label()
        button_1 = Gtk.Button()
        button_2 = Gtk.Button()
        button_3 = Gtk.Button()
        bexit = Gtk.Button('Atras')
        vbox.add(button_0)
        vbox.add(image)
        vbox.add(hbox)
        hbox.add(button_1)
        hbox.add(button_2)
        hbox.add(button_3)
        bboxt = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL)	
        bboxt.set_layout(Gtk.ButtonBoxStyle.CENTER)
        bboxt.add(bexit)
        vbox.add(bboxt)
        bexit.connect('clicked', self.exit,win,menu)
        bboxt.show_all()
        win.show_all()
        self.puntaje=0
        self.numero=random.randint(1,39)
        self.anterior=self.numero
        self.total=0
        button_0.set_text('Comienza a Jugar!!')
        self.parser = SafeConfigParser()
        self.parser.read('trivia.ini')
        
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(self.parser.get('pregunta'+str(self.numero), 'imagen'), 400, 400)
        image.set_from_pixbuf(pixbuf)
        button_1.set_label(self.parser.get('pregunta'+str(self.numero), 'correcta'))
        button_2.set_label(self.parser.get('pregunta'+str (self.numero), 'incorrecta2'))
        button_3.set_label(self.parser.get('pregunta'+str (self.numero), 'incorrecta1'))   
        button_1.connect('clicked',self.__cambiar_imagen_cb, button_2,button_3,button_0,image)
        button_2.connect('clicked',self.__cambiar_imagen_cb, button_3,button_1,button_0,image)
        button_3.connect('clicked',self.__cambiar_imagen_cb, button_2,button_1,button_0,image)
     
    def __cambiar_imagen_cb(self,b1,b2=None,b3=None,b0=None,i=None):
        if b1.get_label()== self.parser.get('pregunta'+ str(self.anterior), 'correcta'):  
            text =self.parser.get('pregunta'+ str(self.anterior), 'correcta')
            p=1
        else:
            p=0
      
        self.puntaje=int(self.puntaje) +p
        
        if self.numero==39:
           self.numero=1
        else:
            self.numero+=1

        if self.numero % 2 ==0:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(self.parser.get('pregunta'+str(self.numero), 'imagen'), 400, 400)
            i.set_from_pixbuf(pixbuf)
            b3.set_label(self.parser.get('pregunta'+str (self.numero), 'correcta'))
            b1.set_label(self.parser.get('pregunta'+str (self.numero), 'incorrecta1'))
            b2.set_label(self.parser.get('pregunta'+str(self.numero), 'incorrecta2'))
           
        else:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(self.parser.get('pregunta'+str(self.numero), 'imagen'), 400, 400)
            i.set_from_pixbuf(pixbuf)
            b3.set_label(self.parser.get('pregunta'+str (self.numero), 'incorrecta1'))
            b1.set_label(self.parser.get('pregunta'+str (self.numero), 'incorrecta2'))
            b2.set_label(self.parser.get('pregunta'+str(self.numero), 'correcta'))
            palabra = 'correcta' if self.puntaje==1 else 'correctas'
          
            self.anterior=self.numero
            self.total= int(self.total)+1
            b0.set_label('%d %s de %d' % (self.puntaje, palabra, self.total))

    def read_file(self, tmp_file):
        self.puntaje=self.metadata["puntaje"]
        self.total=self.metadata["total"]
        self.numero=self.metadata["numero"]
        self.anterior=self.metada["anterior"]  

    def write_file(self, tmp_file):
        self.metadata["numero"]=self.numero
        self.metadata["anterior"]=self.anterior
        self.metadata["total"]=self.total
        self.metadata["puntaje"]=self.puntaje
 
    def main(self):
        Gtk.main()

print __name__
if __name__ == "__main__": 
    base = Base()  
    base.main()
