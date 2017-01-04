#!/usr/bin/env python
# -*- coding:utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')

import random
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from ConfigParser import SafeConfigParser
import json


class Base(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, Gtk.WindowType.TOPLEVEL)
        self.connect("delete-event", Gtk.main_quit)
        # Uso un scroll como solución a los problemas de resolución
        self.scroll = Gtk.ScrolledWindow()
        self.scroll.set_policy(
            Gtk.PolicyType.AUTOMATIC,
            Gtk.PolicyType.AUTOMATIC)
        # Uso un widget principal para los problemas de resolución x2..
        self.widget_principal = Gtk.EventBox()

        self.scroll.add_with_viewport(self.widget_principal)
        self.conociendo = None
        self.menu = None

        self.maximize()

        self.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse("white"))
        self.entrar_a_menu()

        self.add(self.scroll)
        self.show_all()

    def entrar_a_menu(self, widget=None):
        if not self.menu:
            self.crear_menu()

        self.limpiar_ventana()
        self.widget_principal.add(self.menu)
        self.show_all()

    def crear_menu(self):
        self.limpiar_ventana()

        # Parser
        parser = SafeConfigParser()
        parser.read('Config.ini')

        self.menu = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        title = Gtk.Label('Senales de transito')
        inicio = Gtk.Image()
        conoce = Gtk.Button(parser.get('botones', 'a'))
        sabes = Gtk.Button(parser.get('botones', 'b'))
        sabias = Gtk.Button(parser.get('botones', 'c'))
        # self.fondo = Gtk.EventBox()
        # self.fondo.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse('White'))

        # Conexiones
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(
            'images/inicio.gif', 250, 250)
        inicio.set_from_pixbuf(pixbuf)
        conoce.connect('clicked', self.conoceme)
        sabes.connect('clicked', self.initi)
        sabias.connect('clicked', self.futurista)

        # Diseno
        self.menu.pack_start(title, False, False, 5)
        self.menu.pack_start(inicio, True, True, 10)
        self.menu.pack_start(conoce, False, False, 5)
        self.menu.pack_start(sabes, False, False, 5)
        self.menu.pack_start(sabias, False, False, 5)

    def conoceme(self, widget):
        if not self.conociendo:
            self.crear_widget_conoceme()

        self.limpiar_ventana()
        self.widget_principal.add(self.conociendo)
        self.show_all()

    def crear_widget_conoceme(self):
        self.conociendo = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        informativas_frame = Gtk.Frame(label='Informativas')
        informativas_frame.set_shadow_type(Gtk.ShadowType.ETCHED_OUT)
        informativas_frame.set_size_request(250, 300)
        informativas_frame.props.margin = 10

        preventivas_frame = Gtk.Frame(label='Preventivas')
        preventivas_frame.set_shadow_type(Gtk.ShadowType.ETCHED_OUT)
        preventivas_frame.set_size_request(250, 300)
        preventivas_frame.props.margin = 10

        reglamentarias_frame = Gtk.Frame(label='Reglamentarias')
        reglamentarias_frame.set_shadow_type(Gtk.ShadowType.ETCHED_OUT)
        reglamentarias_frame.set_size_request(250, 300)
        reglamentarias_frame.props.margin = 10

        self.conociendo.pack_start(informativas_frame, False, False, 0)
        self.conociendo.pack_start(preventivas_frame, False, False, 0)
        self.conociendo.pack_start(reglamentarias_frame, False, False, 0)

        # Conexiones
        salir = Gtk.Button('Inicio')
        salir.set_size_request(30, 30)
        salir.connect('clicked', self.entrar_a_menu)

        informativas = Gtk.Grid()
        preventivas = Gtk.Grid()
        reglamentarias = Gtk.Grid()

        # ScrolledWindow's para los grids.
        scrolled_informativas = Gtk.ScrolledWindow()
        scrolled_informativas.set_border_width(10)
        scrolled_informativas.add_with_viewport(informativas)
        informativas_frame.add(scrolled_informativas)

        scrolled_preventivas = Gtk.ScrolledWindow()
        scrolled_preventivas.set_border_width(10)
        scrolled_preventivas.add_with_viewport(preventivas)
        preventivas_frame.add(scrolled_preventivas)

        scrolled_reglamentarias = Gtk.ScrolledWindow()
        scrolled_reglamentarias.set_border_width(10)
        scrolled_reglamentarias.add_with_viewport(reglamentarias)
        reglamentarias_frame.add(scrolled_reglamentarias)

        self.conociendo.pack_start(informativas_frame, False, False, 0)
        self.conociendo.pack_start(preventivas_frame, False, False, 0)
        self.conociendo.pack_start(reglamentarias_frame, False, False, 0)

        salir_bbox = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL)
        salir_bbox.set_layout(Gtk.ButtonBoxStyle.CENTER)
        salir_bbox.add(salir)
        salir_bbox.props.margin = 10
        self.conociendo.pack_end(salir_bbox, False, False, 0)

        # señales, cargadas desde el archivo json
        f = open("senales.json", "r")
        seniales = json.load(f)
        f.close()

        for senial in seniales:
            path, x, y, tipo = seniales[senial]

            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(path, 32, 32)
            imagen = Gtk.Image.new_from_pixbuf(pixbuf)
            boton = Gtk.Button()
            boton.add(imagen)
            boton.set_tooltip_text(senial)
            boton.connect(
                'clicked',
                self.detalle,
                senial)

            grids = {"Reglamentaria": reglamentarias,
                     "Informativa": informativas,
                     "Preventiva": preventivas}
            grids[tipo].attach(boton, x, y, 1, 1)

            boton.show_all()

    def limpiar_ventana(self):
        for widget in self.widget_principal.get_children():
            self.widget_principal.remove(widget)

    def detalle(self, boton, data):
        self.limpiar_ventana()

        parser = SafeConfigParser()
        parser.read('Config.ini')

        detalle = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        titulo = Gtk.Label(parser.get(data, 'titulo'))

        info = Gtk.TextView()
        info.set_wrap_mode(Gtk.WrapMode.WORD)
        info.set_editable(False)

        textbuffer = info.get_buffer()
        textbuffer.set_text(parser.get(data, 'info'))
        quit = Gtk.Button('Salir')

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(
            parser.get(data, 'image'), 250, 250)

        imagesenal = Gtk.Image.new_from_pixbuf(pixbuf)

        quit.connect('clicked', self.conoceme)

        detalle.pack_start(titulo, False, False, 0)
        detalle.pack_start(imagesenal, False, False, 10)
        detalle.pack_start(info, True, True, 10)
        detalle.pack_start(quit, False, False, 5)

        self.widget_principal.add(detalle)
        self.show_all()

    def futurista(self, widget):
        self.limpiar_ventana()

        ran = random.randint(1, 6)
        parser = SafeConfigParser()
        parser.read('Config.ini')
        historia = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        title = Gtk.Label(parser.get('historia' + str(ran), 'title'))

        imagehistory = Gtk.Image()
        infohistory = Gtk.TextView()
        infohistory.set_wrap_mode(Gtk.WrapMode.WORD)
        infohistory.set_editable(False)

        textbuffer = infohistory.get_buffer()
        textbuffer.set_text(parser.get('historia' + str(ran), 'h'))

        quiti = Gtk.Button('Salir')
        quiti.connect('clicked', self.entrar_a_menu)

        historia.pack_start(title, False, False, 0)
        historia.pack_start(imagehistory, False, False, 10)
        historia.pack_start(infohistory, True, True, 10)
        historia.pack_start(quiti, False, False, 0)

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(
            parser.get('historia' + str(ran), 'image'), 250, 250)
        imagehistory.set_from_pixbuf(pixbuf)

        self.widget_principal.add(historia)
        self.show_all()

    def initi(self, widget):
        self.limpiar_ventana()

        image = Gtk.Image()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        button_0 = Gtk.Label()
        button_1 = Gtk.Button()
        button_2 = Gtk.Button()
        button_3 = Gtk.Button()

        bexit = Gtk.Button('Atras')
        vbox.pack_start(button_0, False, False, 0)
        vbox.pack_start(image, True, True, 15)
        vbox.pack_start(hbox, False, False, 15)

        hbox.pack_start(button_1, True, True, 0)
        hbox.pack_start(button_2, True, True, 0)
        hbox.pack_start(button_3, True, True, 0)

        bboxt = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL)
        bboxt.set_layout(Gtk.ButtonBoxStyle.CENTER)
        bboxt.add(bexit)
        bexit.connect('clicked', self.entrar_a_menu)

        vbox.pack_start(bboxt, True, True, 0)

        self.puntaje = 0
        self.numero = random.randint(1, 39)
        self.anterior = self.numero
        self.total = 0
        button_0.set_text('Comienza a Jugar!!')
        self.parser = SafeConfigParser()
        self.parser.read('trivia.ini')

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(
            self.parser.get('pregunta' + str(self.numero), 'imagen'), 250, 250)
        image.set_from_pixbuf(pixbuf)
        button_1.set_label(self.parser.get(
            'pregunta' + str(self.numero), 'correcta'))
        button_2.set_label(self.parser.get(
            'pregunta' + str(self.numero), 'incorrecta2'))
        button_3.set_label(self.parser.get(
            'pregunta' + str(self.numero), 'incorrecta1'))
        button_1.connect(
            'clicked',
            self.__cambiar_imagen_cb,
            button_2,
            button_3,
            button_0,
            image)
        button_2.connect(
            'clicked',
            self.__cambiar_imagen_cb,
            button_3,
            button_1,
            button_0,
            image)
        button_3.connect(
            'clicked',
            self.__cambiar_imagen_cb,
            button_2,
            button_1,
            button_0,
            image)

        self.widget_principal.add(vbox)
        self.show_all()

    def __cambiar_imagen_cb(self, b1, b2=None, b3=None, b0=None, i=None):
        if b1.get_label() == self.parser.get('pregunta' + str(self.anterior), 'correcta'):
            text = self.parser.get('pregunta' + str(self.anterior), 'correcta')
            p = 1
        else:
            p = 0

        self.puntaje = int(self.puntaje) + p

        if self.numero == 39:
            self.numero = 1
        else:
            self.numero += 1

        if self.numero % 2 == 0:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(
                self.parser.get('pregunta' + str(self.numero), 'imagen'), 250, 250)
            i.set_from_pixbuf(pixbuf)
            b3.set_label(self.parser.get(
                'pregunta' + str(self.numero), 'correcta'))
            b1.set_label(self.parser.get(
                'pregunta' + str(self.numero), 'incorrecta1'))
            b2.set_label(self.parser.get(
                'pregunta' + str(self.numero), 'incorrecta2'))

        else:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(
                self.parser.get('pregunta' + str(self.numero), 'imagen'), 250, 250)
            i.set_from_pixbuf(pixbuf)
            b3.set_label(self.parser.get(
                'pregunta' + str(self.numero), 'incorrecta1'))
            b1.set_label(self.parser.get(
                'pregunta' + str(self.numero), 'incorrecta2'))
            b2.set_label(self.parser.get(
                'pregunta' + str(self.numero), 'correcta'))
            palabra = 'correcta' if self.puntaje == 1 else 'correctas'

            self.anterior = self.numero
            self.total = int(self.total) + 1
            b0.set_label('%d %s de %d' % (self.puntaje, palabra, self.total))

    def read_file(self, tmp_file):
        self.puntaje = self.metadata["puntaje"]
        self.total = self.metadata["total"]
        self.numero = self.metadata["numero"]
        self.anterior = self.metada["anterior"]

    def write_file(self, tmp_file):
        self.metadata["numero"] = self.numero
        self.metadata["anterior"] = self.anterior
        self.metadata["total"] = self.total
        self.metadata["puntaje"] = self.puntaje

    def main(self):
        Gtk.main()


if __name__ == "__main__":
    base = Base()
    base.main()
