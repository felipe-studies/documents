#!/bin/bash
gcc `pkg-config --cflags gtk+-3.0` -o gtk-example-0 gtk-example-0.c `pkg-config --libs gtk+-3.0`
gcc `pkg-config --cflags gtk+-3.0` -o gtk-example-1 gtk-example-1.c `pkg-config --libs gtk+-3.0`