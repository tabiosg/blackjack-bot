import pyautogui
import win32api
import win32con
from pyautogui import *


# These functions are specific to the Casino Stars Season 2 game on Facebook


def click(x, y) -> None:
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def location_contains_image_color_matters(num1, num2, num3, num4, image_location) -> bool:
    return pyautogui.locateOnScreen(image_location,
                                    region=(num1, num2, num3, num4), grayscale=False, confidence=0.95) is not None


def location_contains_image_color_matters_not(num1, num2, num3, num4, image_location) -> bool:
    return pyautogui.locateOnScreen(image_location,
                                    region=(num1, num2, num3, num4), grayscale=True, confidence=0.95) is not None


def re_bet_option_is_available() -> bool:
    return location_contains_image_color_matters(1300, 850, 600, 250, r"images\identifiers\re_bet.png")


def click_re_bet_option() -> None:
    click(1447, 981)
    return


def click_collect_pop_up() -> None:
    click(958, 787)
    return


def split_is_available() -> bool:
    return location_contains_image_color_matters(1300, 850, 600, 250, r"images\identifiers\split.png")


def it_is_player_turn() -> bool:
    return location_contains_image_color_matters(1300, 850, 600, 250, r"images\identifiers\hit.png")


def read_dealer_number() -> str:
    if location_contains_image_color_matters_not(800, 130, 200, 200, r"images\dealer_number\A.png"):
        return "A"
    if location_contains_image_color_matters_not(800, 130, 200, 200, r"images\dealer_number\2.png"):
        return "2"
    if location_contains_image_color_matters_not(800, 130, 200, 200, r"images\dealer_number\3.png"):
        return "3"
    if location_contains_image_color_matters_not(800, 130, 200, 200, r"images\dealer_number\4.png"):
        return "4"
    if location_contains_image_color_matters_not(800, 130, 200, 200, r"images\dealer_number\5.png"):
        return "5"
    if location_contains_image_color_matters_not(800, 130, 200, 200, r"images\dealer_number\6.png"):
        return "6"
    if location_contains_image_color_matters_not(800, 130, 200, 200, r"images\dealer_number\7.png"):
        return "7"
    if location_contains_image_color_matters_not(800, 130, 200, 200, r"images\dealer_number\8.png"):
        return "8"
    if location_contains_image_color_matters_not(800, 130, 200, 200, r"images\dealer_number\9.png"):
        return "9"
    return "10"


def read_player_number() -> str:
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\4.png"):
        return "4"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\5.png"):
        return "5"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\6.png"):
        return "6"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\7.png"):
        return "7"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\8.png"):
        return "8"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\9.png"):
        return "9"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\10.png"):
        return "10"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\11.png"):
        return "11"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\12.png"):
        return "12"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\13.png"):
        return "13"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\14.png"):
        return "14"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\15.png"):
        return "15"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\16.png"):
        return "16"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\17.png"):
        return "17"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\18.png"):
        return "18"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\19.png"):
        return "19"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\20.png"):
        return "20"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\12_soft.png"):
        return "12_soft"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\13_soft.png"):
        return "13_soft"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\14_soft.png"):
        return "14_soft"

    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\15_soft.png"):
        return "15_soft"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\16_soft.png"):
        return "16_soft"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\17_soft.png"):
        return "17_soft"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\18_soft.png"):
        return "18_soft"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\19_soft.png"):
        return "19_soft"
    if location_contains_image_color_matters_not(800, 410, 200, 100, r"images\player_number\20_soft.png"):
        return "20_soft"


def go_hit() -> None:
    click(1627, 984)
    return


def go_surrender() -> None:
    click(1249, 981)
    return


def go_double_down() -> None:
    click(1447, 981)
    return


def go_stand() -> None:
    click(1810, 975)
    return


def go_split() -> None:
    click(973, 669)
    return
