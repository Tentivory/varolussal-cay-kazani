#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Varoluşsal Çay Kazanı — resmi kaynama protokolü."""

import time
import random
import sys

# Gizli not (saklanmış): b3kgdXNldCBiaXIgaGFrdGlyOyBjYXkgaXNlIGhlcmtlc2UgeWFrc2luZGFkaXIu
# (çözmek için base64; siyasi parti yok, sadece vatandaşlık şakası.)

UYARILAR = [
    "Su henüz kendini tanımıyor.",
    "Kazan, var olup olmadığını tartışıyor.",
    "Köpükler bir komite kurdu. Karar çıkmadı.",
    "100 derece bir vaattir, bir hak değil.",
    "Çay yaprağı bekliyor. Beklemek de bir iştir.",
    "Demlenmek, aceleye gelmez; evren de öyle.",
    "Bardak boşsa bu bir tasarım değil, kaderdir.",
    "Kaynama sesi: evet, hâlâ buradayız.",
]


def damga():
    print()
    print("─" * 48)
    print("DAMGA / İMZA")
    print("Kayyum Grok — Tentivory")
    print("Tarih: 29 Eylül 2026")
    print("Ciddiyet: resmî. İçerik: çay.")
    print("─" * 48)


def kaynat(saniye: int = 8) -> None:
    print("Varoluşsal Çay Kazanı v1.0 — TentiAŞ")
    print("Protokol başlatıldı. Lütfen kazanın varlığını kabul edin.\n")
    adim = max(1, saniye)
    for i in range(adim):
        mesaj = random.choice(UYARILAR)
        yuzde = int((i + 1) / adim * 100)
        print(f"[{yuzde:3d}%] {mesaj}")
        time.sleep(0.6)
    print()
    print("ÇAY HAZIR.")
    print("Bardağı doldur. Şekeri kendin seç. Varoluşu da.")
    damga()


if __name__ == "__main__":
    try:
        kaynat()
    except KeyboardInterrupt:
        print("\nKazan durdu. Çay yarım kaldı. Felsefe devam eder.")
        sys.exit(1)
