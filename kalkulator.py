#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 20:57:01 2020

@author: taufiq
"""

def tambah (a ,b):
    tambah = float(a) + float(b)
    return tambah
def kurang (a ,b):
    kurang = float(a) + float(b)
    return kurang
def kali (a ,b):
    kali = float(a) + float(b)
    return kali
def bagi (a ,b):
    bagi = float(a) + float(b)
    return bagi

while True:
    print("====== kalkulator ======")
    a = input("masukan bilangan 1: ")
    b = input("masukan bilangan 2: ")
    print("\n1. penjumlahan \n2. pengurangan \n3. pembagian \n4. perkalian \n5. batal")
    c = input("\npilih 1 - 5: ")
    if c == "1":
        print("hasil bilangan: ",tambah (a, b))
    elif c == "2":
        print("hasil bilangan: ",kurang (a, b))
    elif c == "3":
        print("hasil bilangan: ",kali (a, b))
    elif c == "4":
        print("hasil bilangan: ",bagi (a, b))
    elif c == "5":
        break
    else:
        print("oprasi error")