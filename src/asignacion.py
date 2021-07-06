# -*- coding: utf-8 -*-

def asignacion(parcelas, cultivos, asign):
    _show_introduccion_message()

    if parcelas == {} or cultivos == {}:
        _show_need_one_pacela_and_one_cultivo_message()
        return

    for parcela in parcelas:
        for cultivo in cultivos:
            _asignate_parcela_to_cultivo(parcelas, cultivos, parcela, cultivo, asign)

    _sort_and_update(asign)

    if asign == {}:
        _show_no_asignations_message()


def _asignate_parcela_to_cultivo(parcelas, cultivos, parcela, cultivo, asign):
    if parcelas[parcela][0] != cultivos[cultivo][0]:
        return
    if parcelas[parcela][1] > cultivos[cultivo][3]:
        return
    if parcela in asign.values():
        return
    if cultivo in asign:
        return

    _show_asign_message(parcela, cultivo)
    asign.update({cultivo: parcela})


def _sort_and_update(asign):
    asign_sorted = sorted(asign.items())
    asign.clear()
    for asignacion in range(len(asign_sorted)):
        asign.update({asign_sorted[asignacion][0]: asign_sorted[asignacion][1]})


def _show_asign_message(parcela, cultivo):
    print('Se asigna el cultivo', cultivo, 'a la parcela', parcela, '\n')


def _show_need_one_pacela_and_one_cultivo_message():
    print('No se pueden realizar asignaciones.')
    print('Para ello debe haber al menos una parcela y un cultivo registrado en el sistema.')


def _show_introduccion_message():
    print('\nHa seleccionado la simulación Asiganción de Cultivos.\n')
    print('\nASIGNACION DE CULTIVOS\n')


def _show_no_asignations_message():
    print('No se han producido asignaciones.')
