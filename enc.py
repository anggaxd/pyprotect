ó
ae_c        
   @   s  d  d l  Z  d  d l Z d  d l m Z d  d l m Z d Z d Z d Z d Z	 d Z
 d	 Z d
 Z e j d  e GHy
 e Z Wn e k
 r n Xd d d d d d d d d d g
 Z d Z d   Z d   Z d   Z d   Z e d k re   Z e e j e j  n  d S(   iÿÿÿÿN(   t   OrderedDict(   t   pformatt   anggaxds#   Github : https://github.com/anggaxds   [34ms   [31ms   [0ms   [33;5ms½  
     [31m_____       _____           _            _   
    [31m|  __ \     |  __ \         | |          | |  
    [31m| |__) |   _| |__) | __ ___ | |_ ___  ___| |_ 
    [31m|  ___/ | | |  ___/ '__/ _ \| __/ _ \/ __| __|
    [0m| |   | |_| | |   | | | (_) | ||  __/ (__| |_ 
    [0m|_|    \__, |_|   |_|  \___/ \__\___|\___|\__|
     [0m       __/ |                                 
     [0m      |___/                                  
t   clears   angga kurniawans   ANGGA KURNIAWANt   AVSt   CPt   LOLSZt   ANGGAXDt   ERROR404t   MALASSZt   FOXESSKYiú   c          C   sT   t  j d d  }  |  j d d d t d d |  j d d	 d t d d
 |  j   S(   Nt   descriptionsi   
 Obfuscate your python script by converting an input script to an output script
 Created By : xNot_Founds   -is   --inputt   requiredt   helps   input python script names   -os   --outputs   output python script name(   t   argparset   ArgumentParsert   add_argumentt   Truet
   parse_args(   t   var_args(    (    s   /sdcard/enc_obs.pyt   run_argparse   s    c            s;   d j     f d   t d t      D  j d  S(   Ns   
c         3   s)   |  ] } d  j    | |  ! Vq d S(   s   {}\N(   t   format(   t   .0t   var_x(   t   par_at   par_b(    s   /sdcard/enc_obs.pys	   <genexpr>'   s    i    s   \(   t   joint   ranget   lent   rstrip(   R   R   (    (   R   R   s   /sdcard/enc_obs.pyt   chunk_string&   s    c            sf   t  t |     t  d     j   D  } d j t |  t d j   f d   |  D  t   S(   t    c         s   s!   |  ] \ } } | | f Vq d  S(   N(    (   R   t   var_jt   var_i(    (    s   /sdcard/enc_obs.pys	   <genexpr>-   s    sÉ   #Encrypted By Angga Kurniawan
#Github : https://github.com/anggaxd/
from collections import OrderedDict
exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in
"{}"
.split("  ")])))
s     c         3   s:   |  ]0 } d  j    f d   t t |   D  Vq d S(   t    c         3   s   |  ] }   t  |  Vq d  S(   N(   t   int(   R   t   var_y(   t   var_dict(    s   /sdcard/enc_obs.pys	   <genexpr>.   s    N(   R   t   strt   ord(   R   t   var_z(   R%   (    s   /sdcard/enc_obs.pys	   <genexpr>.   s    (   R    t	   enumeratet   itemsR   R   R   R   t   MAX_STR_LEN(   t   par_1t   par_2t   var_what(    (   R%   s   /sdcard/enc_obs.pyt   encode_string*   s    c         C   sM   t  |   ; } t  | d  # } | j t | j   t   Wd QXWd QXd S(   R   t   wN(   t   opent   writeR/   t   readt	   EMOTICONS(   t   par_3t   par_4t   var_fsrct   var_fdst(    (    s   /sdcard/enc_obs.pyt   main1   s    t   __main__(   R   t   ost   collectionsR    t   pprintR   t   __created__t
   __github__t   Bt   Rt   Wt   Yt   logot   systemt   xrangeR   t	   NameErrorR4   R+   R   R   R/   R9   t   __name__t   argst   inputt   output(    (    (    s   /sdcard/enc_obs.pyt   <module>   s0   

$					