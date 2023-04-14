from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import socket
import struct
import psutil
import random
import time
import ipaddress
 
def bacnet_ack(bvlc_length,npdu_control,max_apdu_size,invoke_id,ack_process_id,apdu_object_identifier,apdu_object_instance,event_ack,seqno,ack_src,stamp):
    
    bvlc_type = 129
    bvlc_function = 10
   
    npdu_version = 1
    
    apdu_type=0
    apdu_service_choice = 0
    context_tag1=9
    context_tag2=28
    context_tag3=41
    tago1=62
    seq_tag=25
    tagc1=63
    c1=74
    strchr=0
    tago2=94
    time_tag=25
    tagc2=95
    
    bacnet_ack =  struct.pack("!BBHBBBBBBBBBHHBBBBBBBBBBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        context_tag1,
        ack_process_id,
        context_tag2,
        apdu_object_identifier,
        apdu_object_instance,
        context_tag3,
        event_ack,
        tago1,
        seq_tag,
        seqno,
        tagc1,
        c1,
        strchr,
        ack_src,
        tago2,
        time_tag,
        stamp,
        tagc2
       )
    return bacnet_ack
    
def bacnet_i_am(bvlc_length,npdu_control,npdu_dst_mac,npdu_dst_mac_length,npdu_hop_count,apdu_object_id,apdu_obj_inst,max_apdu,segment_support,app_vendor_id):
    bvlc_type = 129
    bvlc_function = 10
    
    npdu_version = 1
    
    apdu_type = 16
    apdu_service_choice = 0
    application_tag=196

    apdu_max_tag=34
    app_seg_tag=145
    app_vendor_tag=33
    
    bacnet_i_am =  struct.pack("!BBHBBHBBBBBHHBHBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        npdu_dst_mac, 
        npdu_dst_mac_length,
        npdu_hop_count,
        apdu_type,
        apdu_service_choice,
        application_tag,
        apdu_object_id,
        apdu_obj_inst,
        apdu_max_tag,
        max_apdu,
        app_seg_tag,
        segment_support,
        app_vendor_tag,
        app_vendor_id,
           )
    return bacnet_i_am

def bacnet_unconf_cov(bvlc_length,npdu_control,subscriber_process_id,apdu_device_id,apdu_device_inst,apdu_object_id,apdu_object_inst,propid1,propinst1,propinst2,propid2,propinst3,propinst4):
    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=16
    apdu_service_choice = 2
    context_tag=9
    context_tag1=28
    context_tag2=44
    context_tag3=57
    time_rem=59
    listvalue1a_open=78
    contextprop1=9
    listvalue2a_open=46
    app_prop_tag=68
    listvalue2a_close=47
    contextprop2=9
    listvalue2b_open=46
    app_prop1_tag=68
    listvalue2b_close=47
    listvalue1a_close=79
     
    bacnet_unconf_cov =  struct.pack("!BBHBBBBBBBHHBHHBBBBBBBHHBBBBBHHBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        apdu_service_choice,
        context_tag,
        subscriber_process_id,
        context_tag1,
        apdu_device_id,
        apdu_device_inst,
        context_tag2,
        apdu_object_id,
        apdu_object_inst,
        context_tag3,
        time_rem,
        listvalue1a_open,
        contextprop1,
        propid1,
        listvalue2a_open,
        app_prop_tag,
        propinst1,
        propinst2,
        listvalue2a_close,
        contextprop2,
        propid2,
        listvalue2b_open,
        app_prop1_tag,
        propinst3,
        propinst4,
        listvalue2b_close,
        listvalue1a_close,
       )
    return bacnet_unconf_cov

def bacnet_unconf_event(bvlc_length,npdu_control,processid,apdu_deviceid,apdu_device_inst,apdu_object_id,apdu_object_inst,seqno,notcls,pr,etype,m1,m2,m3,nottype,ackreq,fs,ts,bv,sf):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=16
    apdu_service_choice = 3
    context_tag1=9
    context_tag2=28
    context_tag3=44
    tag1=62
    seq_tag=25
    tag2=63
    nottag=73
    ptag=89
    etagt=105
    mtag=32006
    strchr=0
    ntag=137
    acktag=153   
    fstag=169
    tstag=185
    tago=206
    to_1=30
    to_0=14
    bvt=9
    tc_0=15
    sfct=26
    bt=4
    tc_1=31
    tagc=207
    
    bacnet_unconf_event =  struct.pack("!BBHBBBBBBBHHBHHBBBBBBBBBBHBHHBBBBBBBBBBBBBBBBBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        apdu_service_choice,
        context_tag1,
        processid,
        context_tag2,
        apdu_deviceid,
        apdu_device_inst,
        context_tag3,
        apdu_object_id,
        apdu_object_inst,
        tag1,
        seq_tag,
        seqno,
        tag2,
        nottag,
        notcls,
        ptag,
        pr,
        etagt,
        etype,
        mtag,
        strchr,
        m1,
        m2,
        m3,
        ntag,
        nottype,
        acktag,
        ackreq,
        fstag,
        fs,
        tstag,
        ts,
        tago,
        to_1,
        to_0,
        bvt,
        bv,
        tc_0,
        sfct,
        bt,
        sf,
        tc_1,
        tagc
       )
    return bacnet_unconf_event

def bacnet_unconf_privatet():
    #bvlc
    bvlc_type = 129
    bvlc_function = 10
    bvlc_length = 8
  
    #npdu
    npdu_version = 1
    npdu_control = 0
    
    #apdu
    apdu_type=16
    apdu_service_choice = 4
    
    bacnetunconfpt =  struct.pack("!BBHBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        apdu_service_choice,
        
      )
    return bacnet_unconf_pt
    
def bacnet_time_syn(bvlc_length,npdu_control,date1,date_month,date_day,date_week,time1,time_min,time_secs,time_msecs):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=16
    apdu_service_choice = 6
    app_datetag=164
    app_timetag=180

    bacnet_time_syn =  struct.pack("!BBHBBBBBBBBBBBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        apdu_service_choice,
        app_datetag,
        date1,
        date_month,
        date_day,
        date_week,
        app_timetag,
        time1,
        time_min,
        time_secs,
        time_msecs
        
      )
    return bacnet_time_syn

def bacnet_utctime_syn(bvlc_length,npdu_control,date1,date_month,date_day,date_week,time1,time_min,time_secs,time_msecs):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=16
    apdu_service_choice = 9
    app_datetag=164

    app_timetag=180

    
    bacnet_utctime_syn =  struct.pack("!BBHBBBBBBBBBBBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        apdu_service_choice,
        app_datetag,
        date1,
        date_month,
        date_day,
        date_week,
        app_timetag,
        time1,
        time_min,
        time_secs,
        time_msecs
        
      )
    return bacnet_utctime_syn

def bacnet_who_has(bvlc_length,npdu_control,npdu_dst_mac,npdu_dst_mac_length,npdu_hop_count,device_low_limit,device_high_limit,object_id,object_inst):
  
    bvlc_type = 129
    bvlc_function = 11

    npdu_version = 1

    apdu_type = 16
    apdu_service_choice = 7
    context_tag1=10
    context_tag2=26
    object_context=44

    
    bacnet_who_has =  struct.pack("!BBHBBHBBBBBHBHBHH", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        npdu_dst_mac, 
        npdu_dst_mac_length,
        npdu_hop_count,
        apdu_type,
        apdu_service_choice,
        context_tag1,
        device_low_limit,
        context_tag2,
        device_high_limit,
        object_context,
        object_id,
        object_inst
           )
    return bacnet_who_has

def bacnet_who_has_1(bvlc_length, npdu_control, npdu_dst_mac, npdu_dst_mac_length, npdu_hop_count, apdu_device_low_limit, apdu_device_high_limit, object_id, object_inst):
    bvlc_type = 129
    bvlc_function = 11
    npdu_version = 1
    apdu_type = 16
    apdu_service_choice = 5
    context_tag1 = 0
    context_tag2 = 26
    object_context = 44
    
    bacnet_who_has_1 = struct.pack("!BBHBBHBBBBBHBHBHH", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        npdu_dst_mac, 
        npdu_dst_mac_length,
        npdu_hop_count,
        apdu_type,
        apdu_service_choice,
        context_tag1,
        apdu_device_low_limit,
        context_tag2,
        apdu_device_high_limit,
        object_context,
        object_id,
        object_inst
    )
    return bacnet_who_has_1

def bacnet_who_is_1(bvlc_length, npdu_control, npdu_dst_mac, npdu_dst_mac_length, npdu_hop_count, apdu_device_low_limit, apdu_device_high_limit):
    bvlc_type = 129
    bvlc_function = 11
    npdu_version = 1
    apdu_type = 16
    apdu_service_choice = 8
    apdu_device_low_limit_length = 12
    apdu_device_high_limit_length = 28
          
    bacnet_who_is = struct.pack("!BBHBBHBBBBBIBI", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        npdu_dst_mac, 
        npdu_dst_mac_length,
        npdu_hop_count,
        apdu_type,
        apdu_service_choice,
        apdu_device_low_limit_length,
       
        apdu_device_high_limit_length,
        apdu_device_high_limit
    )
    return bacnet_who_is_1


def bacnet_conf_cov(bvlc_length,npdu_control,subscriber_process_id,apdu_device_id,apdu_device_inst,apdu_object_id,apdu_object_inst,prop_id_1,prop_inst_1,prop_inst_2,prop_id_2,prop_inst_3,prop_inst_4):

    bvlc_type = 129
    bvlc_function = 10
 
    npdu_version = 1

    apdu_type=0
    max_apdu=3
    invoke_id=75
    apdu_service_choice = 1
    context_tag=9
    context_tag1=28
    context_tag2=44
    context_tag3=57
    time_rem=59
    listvalue1a_open=78
    contextprop1=9
    listvalue2a_open=46
    app_prop_tag=68
    listvalue2a_close=47
    contextprop2=9
    listvalue2b_open=46
    app_prop1_tag=68
    listvalue2b_close=47
    listvalue1a_close=79
      
    bacnet_conf_cov =  struct.pack("!BBHBBBBBBBBBHHBHHBBBBBBBHHBBBBBHHBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu,
        invoke_id,
        apdu_service_choice,
        context_tag,
        subscriber_process_id,
        context_tag1,
        apdu_device_id,
        apdu_device_inst,
        context_tag2,
        apdu_object_id,
        apdu_object_inst,
        context_tag3,
        time_rem,
        listvalue1a_open,
        contextprop1,
        prop_id_1,
        listvalue2a_open,
        app_prop_tag,
        prop_inst_1,
        prop_inst_2,
        listvalue2a_close,
        contextprop2,
        prop_id_2,
        listvalue2b_open,
        app_prop1_tag,
        prop_inst_3,
        prop_inst_4,
        listvalue2b_close,
        listvalue1a_close,
       )
    return bacnet_conf_cov

def bacnet_conf_event(bvlc_length,npdu_control,processid,apdu_device_id,apdu_device_inst,apdu_object_id,apdu_object_inst,seqno,notcls,pr,etype,m1,m2,m3,nottype,ackreq,fs,ts,bv,sf):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=0
    max_apdu= 3
    invoke_id=71
    apdu_service_choice = 2
    context_tag1=9
    context_tag2=28
    context_tag3=44
    tag1=62
    seq_tag=25
    tag2=63
    nottag=73
    ptag=89
    etagt=105
    mtag=32006
    strchr=0
    ntag=137
    acktag=153
    fstag=169
    tstag=185
    tago=206
    to_1=30
    to_0=14
    bvt=9
    tc_0=15
    sfct=26
    bt=4
    tc_1=31
    tagc=207
    
    
    bacnet_conf_event =  struct.pack("!BBHBBBBBBBBBHHBHHBBBBBBBBBBHBHHBBBBBBBBBBBBBBBBBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu,
        invoke_id,
        apdu_service_choice,
        context_tag1,
        processid,
        context_tag2,
        apdu_device_id,
        apdu_device_inst,
        context_tag3,
        apdu_object_id,
        apdu_object_inst,
        tag1,
        seq_tag,
        seqno,
        tag2,
        nottag,
        notcls,
        ptag,
        pr,
        etagt,
        etype,
        mtag,
        strchr,
        m1,
        m2,
        m3,
        ntag,
        nottype,
        acktag,
        ackreq,
        fstag,
        fs,
        tstag,
        ts,
        tago,
        to_1,
        to_0,
        bvt,
        bv,
        tc_0,
        sfct,
        bt,
        sf,
        tc_1,
        tagc,
       )
    return bacnet_conf_event
 
def bacnet_conf_privatet():

    bvlc_type = 129
    bvlc_function = 10
    bvlc_length = 8

    npdu_version = 1
    npdu_control = 0
    
    apdu_type=10
    apdu_service_choice = 4
    
    bacnet_conf_pt =  struct.pack("!BBHBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        apdu_service_choice,
        
      )
    return bacnet_conf_pt 
    
def bacnet_alarm(bvlc_length,npdu_control,max_apdu_size,invoke_id):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=0
    apdu_service_choice = 3
     
    bacnetalarm=  struct.pack("!BBHBBBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
       )
    return bacnet_alarm

def bacnet_enroll(bvlc_length,npdu_control,max_apdu_size,invoke_id,ack_filter,rece_obj_id,rece_obj_inst,process_id,state_filter,type_filter):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=0
    apdu_service_choice = 4
    tag1_open=30
    tag2_open=14
    recipient=12
    tag2_close=15
    tag1_close=31
    state_tag=41
    type_tag=57
 
    bacnet_event=  struct.pack("!BBHBBBBBBHBBBHHBHBBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        ack_filter,
        tag1_open,
        tag2_open,
        recipient,
        rece_obj_id,
        rece_obj_inst,
        tag2_close,
        process_id,
        tag1_close,
        state_tag,
        state_filter,
        type_tag,
        type_filter
       )
    return bacnet_event  

def bacnet_cov(bvlc_length,npdu_control,max_apdu_size,invoke_id,subscriber_processid,apdu_object_identifier,apdu_object_instance,issue_notification,context_tag3,life_time):
   
    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1
    
    apdu_type=0
    apdu_service_choice = 5
    context_tag=9
    context_tag1=28
    context_tag2=41
      
    bacnet_cov =  struct.pack("!BBHBBBBBBBBBHHBBBH", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        context_tag,
        subscriber_processid,
        context_tag1,
        apdu_object_identifier,
        apdu_object_instance,
        context_tag2,
        issue_notification,
        context_tag3,
        life_time
       )
    return bacnet_cov

def bacnet_read_file(bvlc_length,npdu_control,max_apdu_size,invoke_id,apdu_object_identifier,apdu_object_instance,start_rec,req_rec_count):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=0
    apdu_service_choice = 6
    context_tag=12
    record_tag1=14
    startrec_tag=49
    reqrec_count_tag=33
    record_tag2=15
    
    bacnet_a_read_file =  struct.pack("!BBHBBBBBBBHHBBBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        context_tag,
        apdu_object_identifier,
        apdu_object_instance,
        record_tag_1,
        start_rec_tag,
        start_rec,
        reqrec_count_tag,
        req_rec_count,
        record_tag2,
    )
    return bacnet_a_read_file

def bacnet_write_file(bvlc_length,npdu_control,max_apdu_size,invoke_id,apdu_object_identifier,apdu_object_instance,start_rec,req_rec_count):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=0
    apdu_service_choice = 7
    context_tag=12
    record_tag1=14
    start_rec_tag=49
    req_rec_count_tag=33
    record_tag2=15
    
      
    bacnet_a_write_file =  struct.pack("!BBHBBBBBBBHHBBBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        context_tag,
        apdu_object_identifier,
        apdu_object_instance,
        record_tag1,
        start_rec_tag,
        start_rec,
        reqrec_count_tag,
        req_rec_count,
        record_tag2,
       )
    return bacnet_a_write_file

def bacnet_add_list(bvlc_length,npdu_control,max_apdu_size,invoke_id,apdu_object_identifier,apdu_object_instance,property_id,prop_value1,prop_value2):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=0
    apdu_service_choice = 8
    context_tag1=12
    context_tag2=25
    tag_open=62
    app_prop_tag=68
    tag_close=63
      
    bacnet_add_list =  struct.pack("!BBHBBBBBBBHHBBBBHHB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        context_tag1,
        apdu_object_identifier,
        apdu_object_instance,
        context_tag2,
        property_id,
        tag_open,
        app_prop_tag,
        prop_value1,
        prop_value2,
        tag_close
       )
    return bacnet_add_list

def bacnet_remove_list(bvlc_length,npdu_control,max_apdu_size,invoke_id,apdu_object_identifier,apdu_object_instance,property_id,prop_value1,prop_value2):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=0
    apdu_service_choice = 9
    context_tag1=12
    context_tag2=25
    tag_open=62
    app_prop_tag=68
    tag_close=63
      
    bacnet_remove_list =  struct.pack("!BBHBBBBBBBHHBBBBHHB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        context_tag1,
        apdu_object_identifier,
        apdu_object_instance,
        context_tag2,
        property_id,
        tag_open,
        app_prop_tag,
        prop_value1,
        prop_value2,
        tag_close
       )
    return bacnet_remove_list

def bacnet_create(bvlc_length,npdu_control,max_apdu_size,invoke_id,apdu_object_identifier,apdu_object_instance,property_identifier):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=0
    apdu_service_choice = 10
    class_tag=14
    context_tag=28
    class_tag1=15
    open_tag=39
    context_tag1=9
    tag1=46
    tag2=47
    close_tag=31
     
    bacnet_create =  struct.pack("!BBHBBBBBBBBHHBBBBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        class_tag,
        context_tag,
        apdu_object_identifier,
        apdu_object_instance,
        class_tag1,
        open_tag,
        context_tag1,
        property_identifier,
        tag1,
        tag2,
        close_tag
       )
    return bacnet_create

def bacnet_delete(bvlc_length,npdu_control,max_apdu_size,invoke_id,apdu_object_id,apdu_object_inst):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=0
    apdu_service_choice = 11
    application_tag=196
   
    
    bacnet_delete =  struct.pack("!BBHBBBBBBBHH", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        application_tag,
        apdu_object_id,
        apdu_object_inst
       )
    return bacnet_delete

def bacnet_read_range(bvlc_length,npdu_control,max_apdu_size,invoke_id,apdu_object_identifier,apdu_object_instance,apdu_property_identifier,range_tag1,ref_in,ref_count,range_tag2):

    bvlc_type = 129
    bvlc_function = 10
   

    npdu_version = 1

    apdu_type=0
    apdu_service_choice = 26
    context_tag=12
    context_tag1=25
    ref_in_tag=33
    ref_count_tag=49
 
    bacnet_read_range =  struct.pack("!BBHBBBBBBBHHBBBBBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        context_tag,
        apdu_object_identifier,
        apdu_object_instance,
        context_tag1,
        apdu_property_identifier,
        range_tag1,
        ref_in_tag,
        ref_in,
        ref_count_tag,
        ref_count,
        range_tag2
       )
    return bacnet_read_range

def bacnet_read(bvlc_length,npdu_control,max_apdu_size,invoke_id,apdu_object_identifier,apdu_object_instance,apdu_property_identifier):

    bvlc_type =129
    bvlc_function =10

    npdu_version =1

    apdu_type=0
    apdu_service_choice =12
    context_tag=12
    context_tag1=25
     
    bacnet_read =  struct.pack("!BBHBBBBBBBHHBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        context_tag,
        apdu_object_identifier,
        apdu_object_instance,
        context_tag_1,
        apdu_property_identifier
       )
    return bacnet_read

def Bacnet_read_1(bvlc_length,npdu_control,max_apdu_size,invoke_id,apdu_object_identifier,apdu_object_instance,apdu_property_identifier):

    bvlc_type =129
    bvlc_function =10

    npdu_version =1

    apdu_type=0
    apdu_service_choice =12
    context_tag=12
    
      
    bacnet_read_1 =  struct.pack("!BBHBBBBBBBHHH", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        context_tag,
        apdu_object_identifier,
        apdu_object_instance,
        #context_tag1,
        apdu_property_identifier
       )
    return bacnet_read_1

def bacnet_read_multiple(bvlc_length,npdu_control,max_apdu_size,invoke_id,apdu_object_identifier,apdu_object_instance,apdu_property_identifier1,apdu_property_identifier2,apdu_property_identifier3):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=0
    apdu_service_choice = 14
    context_tag=12
    context_tag1=30
    context_opentag=9
    context_opentag1=9
    context_opentag2=9
    context_closetag=31
    
      
    bacnetreadm =  struct.pack("!BBHBBBBBBBHHBBBBBBBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        context_tag,
        apdu_object_identifier,
        apdu_object_instance,
        context_tag1,
        context_opentag,
        apdu_property_identifier1,
        context_opentag1,
        apdu_property_identifier2,
        context_opentag2,
        apdu_property_identifier3,
        context_closetag
       )
    return bacnet_read_m

def bacnet_write(bvlc_length,max_apdu_size,invoke_id,apdu_object_identifier,apdu_object_instance,apdu_property_identifier,data1,data2):
  
    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1
    npdu_control = 4

    apdu_type=0
    apdu_service_choice = 15
    context_tag=12
    context_tag1=25
    context_tag2=62
    application_tag=68
    context_tag3=63
 
    bacnetwrite =  struct.pack("!BBHBBBBBBBHHBBBBHHB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        context_tag,
        apdu_object_identifier,
        apdu_object_instance,
        context_tag1,
        apdu_property_identifier,
        context_tag2,
        application_tag,
        data1,
        data2,
        context_tag3
       )
    return bacnetwrite

def bacnet_write_m(bvlc_length,npdu_control,max_apdu_size,invoke_id,apdu_object_identifier_1,apdu_object_instance_1,property_id_1,data1,data2,apdu_object_identifier_2,apdu_object_instance_2,property_id_2,data3,data4):
  
    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=0
    apdu_service_choice = 16
    context_taga=12
    context_tag1ao=30
    propertyid1_tag=9
    tag1_open=46
    apptag1=68
    tag1_close=47
    context_tag1ac=31
    
    context_tagb=12
    context_tag1bo=30
    propertyid2_tag=9
    tag2_open=46
    apptag2=68
    tag2_close=47
    context_tag1bc=31
    
    bacnet_write_m =  struct.pack("!BBHBBBBBBBHHBBBBBHHBBBHHBBBBBHHBB", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        context_tag_a,
        apdu_object_identifier_1,
        apdu_object_instance_1,
        context_tag1ao,
        property_id1_tag,
        property_id1,
        tag1_open,
        apptag1,
        data1,
        data2,
        tag1_close,
        context_tag1ac,
        context_tagb,
        apdu_object_identifier_2,
        apdu_object_instance_2,
        context_tag1bo,
        property_id2_tag,
        property_id_2,
        tag2_open,
        app_tag2,
        data3,
        data4,
        tag2_close,
        context_tag_1bc
       )
    return bacnet_write_m

def bacnet_dcc(bvlc_length, max_apdu_size, invoke_id, time_dur, en_dis, passw):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1
    npdu_control = 4

    apdu_type = 0
    apdu_service_choice = 17
    time_tag = 9
    en_distag = 25
    context_tag1 = 42
    string_c = 0  # changed variable name to match regex pattern

    bacnet_dcc = struct.pack("!BBHBBBBBBBBBBBBB",
        bvlc_type,
        bvlc_function,
        bvlc_length,
        npdu_version,
        npdu_control,
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        time_tag,
        time_dur,
        en_distag,
        en_dis,
        context_tag1,
        string_c,  # changed variable name to match regex pattern
        passw
    )
    return bacnet_dcc

def bacnet_rd(bvlc_length, max_apdu_size, invoke_id, device_state, passw):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1
    npdu_control = 4

    apdu_type = 0
    apdu_service_choice = 20
    device_statetag = 9
    context_tag1 = 26
    string_c = 0  # changed variable name to match regex pattern

    bacnet_rd = struct.pack("!BBHBBBBBBBBBBB",
        bvlc_type,
        bvlc_function,
        bvlc_length,
        npdu_version,
        npdu_control,
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        device_statetag,
        device_state,
        context_tag1,
        string_c,  # changed variable name to match regex pattern
        passw
    )
    return bacnet_rd

def bacnet_event_information(bvlc_length,npdu_control,max_apdu_size,invoke_id,apdu_objectidentifier,apdu_objectinstance):

    bvlc_type = 129
    bvlc_function = 10

    npdu_version = 1

    apdu_type=0
    apdu_service_choice = 29
    context_tag=12

    bacnet_event_info=  struct.pack("!BBHBBBBBBBHH", 
        bvlc_type, 
        bvlc_function, 
        bvlc_length, 
        npdu_version,
        npdu_control, 
        apdu_type,
        max_apdu_size,
        invoke_id,
        apdu_service_choice,
        context_tag,
        apdu_object_identifier,
        apdu_object_instance
       )
    return bacnet_event_info
    
s = socket.socket(socket.AF_INET,type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.settimeout(1)


addrs = psutil.net_if_addrs()

valid_port=[*range(0,65535,1)]
bac_validport=[*range(47808,47818,1)]

running=0



#~~~~~~~~~~~~~~~~Main Window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ws = Tk()
ws.title('Protocol Fuzzer')
ws.geometry('750x600')


tabControl = ttk.Notebook(ws)
  
tab1 = ttk.Frame(tabControl)

tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)


st = ttk.Style()
st.configure('TNotebook.Tab', font=('Ariel','10') )
  
tabControl.add(tab1, text ="Device Discovery")
tabControl.add(tab2, text ='Identification',state="disabled")
tabControl.add(tab3, text ='Instrumentation',state='disabled')
tabControl.pack(expand = 2, fill ="both")
  
ttk.Label(tab1, 
          text ="").grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)  
ttk.Label(tab2,
          text ="").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)
ttk.Label(tab3,
          text ="").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)
                                    
                                    


#~~~~~~~~~~~~~~~~~~~~~~~Tab1 : Device_Discovery~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

interface_l=ttk.Label(tab1, text="Interface")
interface_l.place(x=30,y=30)
intf = StringVar()

ipadd=ttk.Combobox(tab1,values=" ",width=20)
ipadd.place(x=150,y=30)

for key in addrs.keys():
    #print(key)
    ipadd['values']+=(key,)

host_ip_l=ttk.Label(tab1, text="Host IP")
host_ip_l.place(x=30,y=80)

host_ip=Entry(tab1,width=15)
host_ip.place(x=150,y=80)

broadcast_ip_l=ttk.Label(tab1, text="Broadcast IP")
broadcast_ip_l.place(x=30,y=130)
bpt = StringVar()
broadcast_ip=ttk.Label(tab1,text=" ")
broadcast_ip.place(x=150,y=130)

target_ip_l=ttk.Label(tab2, text="Target Device IP:")
target_ip_l.place(x=5,y=5)
ipt = StringVar()
target_ip=ttk.Label(tab2,text=" ")
target_ip.place(x=95,y=5)

deviceid_l=ttk.Label(tab2, text="Device ID:")
deviceid_l.place(x=185,y=5)
devid = IntVar()
deviceid=ttk.Label(tab2,text=" ")
deviceid.place(x=250,y=5)

def valid_ip(ip_sub):
    if ("." in ip_sub):
        elements_array = ip_sub.strip().split(".")
        
        if(len(elements_array) == 4):
            for i in elements_array:
                if (i.isnumeric() and int(i)>=0 and int(i)<=255):
                    return ip_sub
        else:
            print('Invalid IP')

def valid_ip1(ip_sub):
      """
      :type IP: str
      :rtype: str
      """
      def isipv4(s):
         try: return str(int(s)) == s and 0 <= int(s) <= 255
         except: return False
      def isipv6(s):
         if len(s) > 4:
            return False
         try : return int(s, 16) >= 0 and s[0] != '-'
         except:
            return False
      if ip_sub.count(".") == 3 and all(isipv4(i) for i in ip_sub.split(".")):
         return ip_sub
      else:
        if ip_sub==host_ip.get():
            messagebox.showerror(title='ERROR',message='Select the Interface')
            host_ip.delete(0, END)
      if ip_sub.count(":") == 7 and all(isipv6(i) for i in ip_sub.split(":")):
         return "IPv6"
      

def host_ipf(event):
    a=str(ipadd.get())
    l1=[]
    if a not in addrs:
        print('Not Present')
    else:
        
        for i in addrs[a]:
            l1.append(i)
        for j in range(len(l1)):
                if l1[j].family == socket.AF_INET:
                    host_ipadd1=l1[j].address
                    net_mask=l1[j].netmask
        netm=ipaddress.IPv4Network(host_ipadd1 +'/'+ net_mask,False)
        bip=netm.broadcast_address
        broadcast_ip.config(text=bip)
        host_ip_add1=valid_ip(host_ipadd1)
        if host_ip.get() is None:
            host_ip.insert(0,host_ip_add1)
        else:
            host_ip.delete(0, END)
            host_ip.insert(0,host_ip_add1)
            

ipadd.bind('<<ComboboxSelected>>',host_ipf)   

   
    
columns = ('1','2')
Dvfound_1=ttk.Treeview(tab1,selectmode='browse',height=10,columns=columns,show='headings')
Dvfound_1.column('1',width=100)
Dvfound_1.column('2',width=100)
Dvfound_1.heading('1', text='Devices_Found')
Dvfound_1.heading('2',text='Device id')
scrollbar = ttk.Scrollbar(tab1,orient="vertical", command=Dvfound_1.yview)
Dvfound_1.configure(yscroll=scrollbar.set)
scrollbar.place(x=535, y=31, height=225)

Dvfound_1.place(x=350,y=30)


def convertbinary(a):
        # initialize an empty string
    #this will print a in binary
    bnr = bin(a).replace('0b','')
    x = bnr[::-1] #this reverses an array
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr
    
def cidr_to_netmask(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask
              
     
proto = ttk.Label(tab1,text="Select a Protocol:")
proto.place(x=30,y=180)
          
var2 = StringVar()
var2.set("None")
data1=("None","BACnet")
cb1=ttk.Combobox(tab1, values=data1,width=15)
cb1.place(x=150, y=180)

portl = ttk.Label(tab1,text="Port:")
portl.place(x=30,y=250)
    
port_no = IntVar()
port_number=Entry(tab1,text=port_no,textvariable=port_no,state="disabled")
port_number.place(x=150,y=250)


def bac_port(event):
    if cb1.get()=='BACnet':
        port_no.set(47808)
        port_number.configure(textvariable=port_no,state="normal")
        
    else:
        port_number.delete(0,END)
        ipadd.delete(0,END)
        list1.delete(0,END)
        list2.delete(0,END)
        for item in table_1.get_children():
            table_1.delete(item)
        
   
cb1.bind("<<ComboboxSelected>>",bac_port)


def device_ip(ip,port):
    for item in Dvfound_1.get_children():
        Dvfound_1.delete(item)
        tab1.update()
    s.bind(('0.0.0.0',47808))
    s.sendto(BacnetWhoIs1(22,32,65535,0,255,0,1,0,65535),(ip,port))
    try:
        while True:
            d1,add=s.recvfrom(4096)
            if d1 is None:
                print('sjd')
            time.sleep(2)
            if d1[5]==0:
                h=hex(int((d1[11]<<8))|int(d1[12]))
                dec=int(h,16)
                if dec==0:
                    return False
                if ((d1[0]==129) and (d1[6]==16) and (d1[7]==0)):
                    Dvfound_1.insert('', index='end',values=(add[0],dec))
                    tab1.update()
            if d1[5]==32:
                h=hex(int((d1[15]<<8))|int(d1[16]))
                dec=int(h,16)
                if dec==0:
                    return False
                if ((d1[0]==129) and (d1[10]==16) and (d1[11]==0)):
                    Dvfound_1.insert('', index='end',values=(add[0],dec))
                    tab1.update()
            
    except socket.timeout:
        print('test')
           
def ip_range(ip,port):
    hostip=host_ip.get()

    ip_range=ip.rsplit('.',1)[-1]
    if ("." in ip):
        ip_add = ip.strip().split(".")
    ip1='.'.join(ip_add[:-1])+'.'
    
    pos=ip_range.split('-',1)
    start=pos[0]
    print(start)
    end=pos[1]
    print(end)
    
    for i in range(int(start),int(end)+1):
        dest_ip=ip1+str(i)
        if(hostip!=dest_ip):
            print(dest_ip)
            try:
                s.sendto(BacnetWhoIs1(22,32,65535,0,255,0,1,0,65535),(dest_ip,port))
                data_range,add_range=s.recvfrom(4096)
                print('Add_range=',add_range)
            except socket.timeout:
                pass
        
def device_sub(ip,port):
    hostip=host_ip.get()
    dv1=cidr_to_netmask(ip)
    ##To Get the subnet mask
    print(dv1[0])
    print(dv1[1])
    masks = [0, 128, 192, 224, 240, 248, 252, 254, 255]
    # Take subnet mask as input
    #input_subnet = input("\nEnter the Subnet Mask: ")
    # Validate the subnet mask
    octet_subnet = [int(j) for j in dv1[1].split(".")]
    if (len(octet_subnet) == 4) and \
        (octet_subnet[0] == 255) and \
        (octet_subnet[1] in masks) and \
        (octet_subnet[2] in masks) and \
        (octet_subnet[3] in masks) and \
        (octet_subnet[0] >= octet_subnet[1] >= octet_subnet[2] >= octet_subnet[3]):
            #break
            print('Valid')  
    else:
            print("Invalid subnet mask, retry\n")
    
    sub_in_bin = []

        # convert each subnet octet to binary
    sub_bin_octet = [bin(i).split("b")[1] for i in octet_subnet]

        # make each binary octet of 8 bit length by padding zeros
    for i in sub_bin_octet:
        if len(i) < 8:
            sub_padded = i.zfill(8)
            sub_in_bin.append(sub_padded)
        else:
            sub_in_bin.append(i)
    sub_bin_mask = "".join(sub_in_bin)

        # calculating number of hosts
    no_zeros = sub_bin_mask.count("0")
    no_ones = 32 - no_zeros
    no_hosts = abs(2 ** no_zeros - 2)
    no_subs=2**abs(24 - no_ones)
    print(no_hosts)
    print(no_subs)
    #print(netid)
    
    
    octet_ip = dv1[0].split(".")
    int_octet_ip = [int(i) for i in octet_ip]
    print('ip=',int_octet_ip)
    ip_in_binary = []

        # Convert each IP octet to binary
    ip_in_bin_octets = [bin(i).split("b")[1] for i in int_octet_ip]
    
        # make each binary octet of 8 bit length by padding zeros
    for i in range(0,len(ip_in_bin_octets)):
        if len(ip_in_bin_octets[i]) < 8:
            padded_bin = ip_in_bin_octets[i].zfill(8)
            ip_in_binary.append(padded_bin)
        else:
            ip_in_binary.append(ip_in_bin_octets[i])

        # join the binary octets
    ip_bin_mask = "".join(ip_in_binary)
    
    network_add_bin = ip_bin_mask[:no_ones] + "0" * no_zeros
    broadcast_add_bin= ip_bin_mask[:no_ones] + "1" * no_zeros
    
    network_add_bin_octet = []
    network_add_octet=[]
    
    broadcast_binoct = []
    broadcast_add_octet=[]
    
    [network_add_bin_octet.append(i) for i in [network_add_bin[j:j+8]
                                                   for j in range(0, len(network_add_bin), 8)]]
    [broadcast_binoct.append(i) for i in [broadcast_add_bin[j:j+8]
                                              for j in range(0,len(broadcast_add_bin),8)]]
    
    network_add_octet=[str(int(i,2)) for i in network_add_bin_octet]
    print(network_add_octet)
    network_add_dec_final = ".".join([str(int(i,2)) for i in network_add_bin_octet])
    
    broadcast_add_octet=[str(int(i,2)) for i in broadcast_binoct]
    print(broadcast_add_octet)
    broadcast_add_dec_final = ".".join([str(int(i,2)) for i in broadcast_binoct])
    print(broadcast_add_dec_final)
    
    first_ip_host = network_add_bin_octet[0:3] + [(bin(int(network_add_bin_octet[3],2)+1).split("b")[1].zfill(8))]
    print('ip_host=',first_ip_host)
    first_ip = ".".join([str(int(i,2)) for i in first_ip_host])
    

    last_ip_host = broadcast_binoct[0:3] + [bin(int(broadcast_binoct[3],2) - 1).split("b")[1].zfill(8)]
    last_ip = ".".join([str(int(i,2)) for i in last_ip_host])
    
    print("IP address range is: {0} - {1}".format(first_ip, last_ip))
    
    print('broadcast_add_oct=',int(broadcast_add_octet[3]))
    periodpos=[]
    for m in re.finditer('\.',first_ip):
        periodpos.append(m.start())
    print(periodpos)
    
    if (len(int_octet_ip) == 4) and \
        (int_octet_ip[0] != 127) and \
        (int_octet_ip[0] != 169):
        print('valid')
        for p in range((int(network_add_octet[3])),(int(broadcast_add_octet[3])),1):
            if (p !=0 and p!=255):
                add='.'+str(p)
                first_ip=first_ip[:periodpos[2]]+add
                #response=os.system("ping -n 1 "+first_ip)
                #if ((response==0) and (first_ip != host_ip)):
                if (first_ip != hostip):
                    
                    print(first_ip)
                   
                    try:
                        #print(first_ip)
                        s.sendto(BacnetWhoIs1(22,32,65535,0,255,0,1,0,65535),(first_ip,port))
                        data_sub,add_sub=s.recvfrom(4096)
                        #print(add_sub)
                        #if address[1]==47808:
                            #ipadd['values'] +=(address[0],)
                            #pass
                    except socket.timeout:
                        pass
                  
    else:
        print("Invalid IP, retry \n")
                
def switch_ip(event,ip,port):
    if ipmode.get()=='IP Address':
        ip1=valid_ip1(ip)
        device_ip(ip1,port)
    elif ipmode.get()=='IP Range':
        print(ipmode.get())
        ip_range(ip,port)
    elif ipmode.get()=='IP Subnet':
        device_sub(ip,port)
    else:
        print('No Selection')
       
def  kr(event):
    if event.widget is dv_btn:
            dv_btn.unbind("<Button-1>")
       
def device_discovery():
    ip=valid_ip(broadcast_ip.cget("text"))
    hp=valid_ip1(host_ip.get())
    if hp is None:
        messagebox.showerror(title='ERROR',message='Host_IP is required')
        
    elif ip is None:
        messagebox.showerror(title='ERROR',message='Broadcast IP is required')
    else:
        if not cb1.get():
            messagebox.showerror(title='ERROR',message='Select the protocol')
        else:
            port=int(port_number.get())
            if port not in valid_port:
                if port not in bac_validport:
                    #print(port)
                    messagebox.showerror(title='ERROR',message='INVALID PORT')
                    port_number.delete(0,END)
            elif port in valid_port:
                if port not in bac_validport:
                    messagebox.showerror(title='ERROR',message='Invalid bacnet port. Kindly provide in the range(47808-47818)')
                    port_number.delete(0,END)
                else:
                    ip1=valid_ip1(ip)
                    device_ip(ip1,port)
                      
def gettarget(event):
    s_item=Dvfound_1.selection()[0]
    item=Dvfound_1.item(s_item)
    value=item['values']
    tabControl.tab(tab2,state="normal")
    tabControl.tab(tab1, state="disabled")
    tabControl.select(tab2)
    target_ip.config(text=value[0])
    deviceid.config(text=value[1])
            

dv_btn = Button(tab1, text="Discovery",width=15, command=device_discovery)
dv_btn.place(x=100,y=330) 

Dvfound_1.bind('<<TreeviewSelect>>',gettarget)

#~~~~~~~~~~~~~~Tab 2: Identification~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ttk.Label(tab2, text="BACnet Services Supported").grid(column=0, row=0, padx=10, pady=10)
list2 = tk.Listbox(tab2,height=12,selectmode='extended')
list2.place(x=180,y=50)
scrollbar2 = ttk.Scrollbar(tab2,orient="vertical", command=list2.yview)
list2.configure(yscroll=scrollbar2.set)
scrollbar2.place(x=290, y=50, height=200)

ttk.Label(tab2, text="BACnet Objects Supported").grid(column=0, row=10, padx=10, pady=200)
list1 = tk.Listbox(tab2,height=12,selectmode='extended')
list1.place(x=180,y=300)
scrollbar1 = ttk.Scrollbar(tab2,orient="vertical", command=list1.yview)
list1.configure(yscroll=scrollbar1.set)
scrollbar1.place(x=290, y=300, height=200)

list3 = tk.Listbox(tab2,height=12,selectmode='extended')
list3.place(x=420,y=50)
scrollbar3 = ttk.Scrollbar(tab2,orient="vertical", command=list3.yview)
list3.configure(yscroll=scrollbar3.set)
scrollbar3.place(x=540, y=50, height=200)

list4 = tk.Listbox(tab2,height=12,selectmode='extended')
list4.place(x=420,y=300)
scrollbar4 = ttk.Scrollbar(tab2,orient="vertical", command=list4.yview)
list4.configure(yscroll=scrollbar4.set)
scrollbar4.place(x=540, y=300, height=200)


def convertbinary(a):
    bnr = bin(a).replace('0b','')
    x = bnr[::-1] 
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr
    
l_service=("Acknowledge Alarm", "Confirmed_Cov", "Confirmed_Event","Alarm Summary", "Enrollment Summary", "COV", "Read File", "Write File", "Add List", "Remove List", "Create Object", "Delete Object", "Read Property", "Read Conditional", "Read Multiple", "Write Property", "Write Multiple", "Device Communication", "Confirmed_Private_Transfer", "Confirmed_Text_Message", "Reinitialize Device", "vtOpen", "vtClose", "vtData", "Authenticate", "Request Key", "I AM", "I Have", "Unconfirmed_Cov", "Unconfirmed_Event", "Unconfirmed_Private", "Unconfirmed_Text", "Time Syncronization", "Who-Has", "Who-Is", "Read Range", "UTC Time Syncronization", "LifeSafety", "COVP", "Event Information", "Write Group")

def bac_services():

    s2 = socket.socket(socket.AF_INET,type=socket.SOCK_DGRAM)
    s2.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    dvid=deviceid.cget("text")
    strd=isinstance(dvid, str)
    
    if strd:
        messagebox.showerror(title='ERROR',message='Target Device IP and DeviceId not received')
    else:
        ip=valid_ip(target_ip.cget("text"))
        port=int(port_number.get())
        
        s2.sendto(Bacnetread1(17,4,68,2,512,dvid,6497),(ip,port))
        dv,add=s2.recvfrom(4096)
        proto_serv= struct.unpack("!BBBBBB",dv[20:26])
        
        serv1=''
        for j in range(len(proto_serv)):
            serv1+=convertbinary(proto_serv[j])
        
        for k in range(len(l_service)):
            if serv1[k]=='1':
                list2.insert(END,l_service[k])
        
    s2.close()
                       
l_object=("Analog_Input", "Analog_Output", "Analog_Value", "Binary_Input", "Binary_Output", "Binary_Value", "Calendar", "Command", "Device", "Event_Enrollment", "File", "Group", "Loop", "Multi_State_Input", "Multi_State_Output", "Notification _Class", "Program", "Schedule", "Averaging", "Multi_State_Value","Trend-Log","Life-Safety-Point","Life-Safety-Zone","Accumulator","Pulse-Converter","Event-Log","Global-Group","Trend-Log-Multiple","Load-Control","Structured-View","Access-Door","Timer","Access-Credential","Access-Point","Access-Rights","Access-User","Access-Zone","Credential-Data-Input","Network-Security","Bitstring-Value","Characterstring-Value","Date-Pattern-Value","Date-Value","Datetime-PatternValue","Datetime-Value","Integer-Value","Large-analog-value","Octectstring-value","Positive-integer-value"
,"Time-pattern-value","Time-value","Notification-forwarder","Alert-Enrollment","Channel","Lighting-Output") 
l_obj1={'Analog_Input':0,'Analog_Output':1, 'Analog_Value':2, 'Binary_Input':3, 'Binary_Output':4, 'Binary_Value':5, 'Calendar':6, 'Command':7, 'Device':8, 'Event_Enrollment':9, 'File':10, 'Group':11, 'Loop':12, 'Multi_State_Input':13, 'Multi_State_Output':14, 'Notification _Class':15, 'Program':16, 'Schedule':17, 'Averaging':18, 'Multi_State_Value':19,'Trend-Log':20,'Life-Safety-Point':21,'Life-Safety-Zone':22,'Accumulator':23,'Pulse-Converter':24,'Event-Log':25,'Global-Group':26,'Trend-Log-Multiple':27,'Load-Control':28,'Structured-View':29,'Access-Door':30,'Timer':31,'Access-Credential':32,'Access-Point':33,'Access-Rights':34,'Access-User':35,'Access-Zone':36,'Credential-Data-Input':37,'Network-Security':38,'Bitstring-Value':39,'Characterstring-Value':40,'Date-Pattern-Value':41,'Date-Value':42,'Datetime-PatternValue':43,'Datetime-Value':44,'Integer-Value':45,'Large-analog-value':46,'Octectstring-value':47,'Positive-integer-value':48
,'Time-pattern-value':49,'Time-value':50,'Notification-forwarder':51,'Alert-Enrollment':52,'Channel':53,'Lighting-Output':54}
#obj1=[]
def bac_objects():

    s3 = socket.socket(socket.AF_INET,type=socket.SOCK_DGRAM)
    s3.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    dvid=deviceid.cget("text")
    strd=isinstance(dvid, str)
    if strd:
        messagebox.showerror(title='ERROR',message='Target Device IP and DeviceId not received')
    else:
        ip=valid_ip(target_ip.cget("text"))
        port=int(port_number.get())
        s3.sendto(Bacnetread1(17,4,68,2,512,dvid,6496),(ip,port))
        dv_data,add=s3.recvfrom(4096)
        st=dv_data.find(62)
        et=dv_data.find(63)
        unbits=dv_data[st+2]
        proto_serv= struct.unpack("!"+str((unbits-1)*'B'), dv_data[et-(unbits-1):et])
        #print(proto_serv)
        serv1=''
        for j in range(len(proto_serv)):
            serv1+=convertbinary(proto_serv[j])
        
        for k in range(len(serv1)):
            if serv1[k]=='1':
                list1.insert(END,l_object[k])
    s3.close()
     
def l1():
    if not list2.get(0,END):
        bac_services()
    else:
        messagebox.showerror(title='ERROR',message='Service List is Not Empty')
        
def l2():
    list2.delete(0,END)
        
def l3():
    if not list1.get(0,END):
        bac_objects()
    else:
        messagebox.showerror(title='ERROR',message='Object List is Not Empty')
        
def l4():
    list1.delete(0,END)
    
def moveto(p,q):
    indexlist = p.curselection()
    if indexlist:
        index = indexlist[0]
        val= p.get(index)
        if((val=="Alarm Summary") or (val=="I AM") or (val=="Who-Is") or (val=="Time Syncronization") or (val=="UTC Time Syncronization") or (val=="Device Communication") or (val=="Reinitialize Device") or (val=="Enrollment Summary")):
            messagebox.showinfo("showinfo","Objects are not required for " + val+  " service" )
        if val not in q.get(0,END):
            q.insert(END,val)
        else:
            messagebox.showerror(title='ERROR',message= val + ' is present')
         
def clearlist(list2):
    index_list = list2.curselection()
    if index_list:
        index = index_list[0]
        list2.delete(index)

def l5():
    list3.delete(ANCHOR)
    
def l6():
    list4.delete(ANCHOR)
    
l1 = Button(tab2, text="Services", height=2, width=10, command=l1)
l1.place(x=40, y=60)

l2 = Button(tab2, text="Clear", height=2, width=10, command=l2)
l2.place(x=40, y=120)

l3 = Button(tab2, text="Objects", height=2, width=10, command=l3)
l3.place(x=40, y=320)

l4 = Button(tab2, text="Clear", height=2, width=10, command=l4)
l4.place(x=40, y=380)

l5 = Button(tab2, text='>>', height=2, width=10, command=lambda: moveto(list2, list3))
l5.place(x=320, y=60)

l6 = Button(tab2, text='>>', height=2, width=10, command=lambda: moveto(list1, list4))
l6.place(x=320, y=320)

l7 = Button(tab2, text='<<', height=2, width=10, command=lambda: clearlist(list3))
l7.place(x=320, y=120)

l8 = Button(tab2, text='<<', height=2, width=10, command=lambda: clearlist(list4))
l8.place(x=320, y=380)




def backb(arg):
    if arg==1:
        tabControl.tab(tab1, state="normal")
        tabControl.tab(tab2, state="disabled")
        tabControl.select(tab1)
        
    if arg==2:
        if running==1:
            list4.configure(state="normal")
            tabControl.tab(tab2, state="normal")
            tabControl.tab(tab3, state="disabled")
            tabControl.select(tab2)
        else:
            messagebox.showerror(title='ERROR',message='Press the Stop Button')
            
def nextb():
    s1=list3.size()
    s2=list4.size()
    if s1==0:
        messagebox.showerror(title='ERROR',message='Select the service')
    for j in range(s1):
        if ((list3.get(j)=="Alarm Summary") or (list3.get(j)=="I AM") or (list3.get(j)=="Who-Is") or (list3.get(j)=="Time Syncronization") or (list3.get(j)=="UTC Time Syncronization")or (list3.get(j)=="Device Communication") or (list3.get(j)=="Reinitialize Device") or (list3.get(j)=="Enrollment Summary") and s2==0):
           list4.configure(state="disabled")
           tabControl.tab(tab3, state="normal")
           tabControl.select(tab3) 
        elif((list3.get(j)=="Acknowledge Alarm" or list3.get(j)=="Who-Has" or list3.get(j)=="Confirmed_Cov" or list3.get(j)=="Confirmed_Event" or list3.get(j)=="Unconfirmed_Private" or list3.get(j)=="COV" or list3.get(j)=="Read File" or list3.get(j)=="Write File" or list3.get(j)=="Add List" or list3.get(j)=="Remove List" or list3.get(j)=="Create Object" or list3.get(j)=="Delete Object" or list3.get(j)=="Read Range" or  list3.get(j)=="Read Property" or list3.get(j)=="Read Multiple" or list3.get(j)=="Write Property" or list3.get(j)=="Write Multiple" or list3.get(j)=="Unconfirmed_Cov" or list3.get(j)=="Unconfirmed_Event" or list3.get(j)=="Unconfirmed_Private" or list3.get(j)=="Event Information") and s2!=0):   
            tabControl.tab(tab3, state="normal")
            tabControl.select(tab3)
        else:
            messagebox.showerror(title='ERROR',message='Select the object')
                           
def tab_change(event):
    tab_1 = event.widget.tab('current')['text']
    if tab_1=='Device Discovery':
        tabControl.tab(tab2,state="disabled")
        tabControl.tab(tab3,state="disabled")
    if tab_1=='Identification':
        tabControl.tab(tab3,state="disabled")
    if tab_1=='Instrumentation':
        tabControl.tab(tab1,state="disabled")
        tabControl.tab(tab2,state="disabled")
           
back_btn1 = Button(tab2, text="Back",height=2,width=10,command=lambda: backb(1))
back_btn1.place(x=0, y=533)

next_btn = Button(tab2, text="Next",height=2,width=10,command=nextb)
next_btn.place(x=660, y=533)

back_btn2 = Button(tab3, text="Back",height=2,width=10,command=lambda: backb(2))
back_btn2.place(x=80, y=230)

tabControl.bind("<<NotebookTabChanged>>",tab_change)

#~~~~~~~~~~~~~~~~~~~~~~Instrumentation~~~~~~~~~~
"""
respti_l=ttk.Label(tab3, text="Response Timeout")
respti_l.place(x=20,y=30)
respi = StringVar()

respt=ttk.Entry(tab3,text=respi,width=15)
respt.place(x=150,y=30)
"""
timed=IntVar()
timedi_l=ttk.Label(tab3, text="Time Delay(ms)")
timedi_l.place(x=20,y=50)
timedi = StringVar()

timedt=ttk.Entry(tab3,text=timed,textvariable=timed,width=15)
timedt.place(x=150,y=50)

def bacnet_ack(ip_address,port_no,timedl,obj):
    bvlen=random.randrange(22,5238)
    npdu_c=4
    max_apdu=random.randrange(0,256)
    invokeid=random.randrange(0,256)
    processid=random.randrange(0,256)
    objid1=random.randrange(0,4000,64)
    objinst=random.randrange(0,65536)
    event_ack=random.randrange(0,256)
    seqn1=random.randrange(0,256)
    acksrc=random.randrange(0,256)
    stamp=random.randrange(0,256)
    count=1
  
    ack=bacnetack(bvlen,npdu_c,max_apdu,invokeid,processid,objid1,objinst,event_ack,seqn1,acksrc,stamp)
  
    for bvlen in range(30,5238):
        if running==0:
            for npdu_c in range(0,80):
                if running==0:
                    for max_apdu in range(0,256):
                        if running==0:
                            for invokeid in range(0,256):
                                if running==0:
                                    for processid in range(0,256):
                                        if running==0:
                                            for m in range(len(obj)):
                                                if running==0:
                                                    for objinst in range(0,65536):
                                                        if running==0:
                                                            for event_ack in range(0,256):
                                                                if running==0:
                                                                    for seqn1 in range(0,256):
                                                                        if running==0:
                                                                            for acksrc in range(0,256):
                                                                                if running==0:
                                                                                    for stamp in range(0,256):
                                                                                        if ((ack[0]==129) and (ack[1]==10) and (ack[6]==0) and (ack[9]==0) and (ack[10]==9) and (ack[12]==28) and (ack[17]==41) and (ack[19]==62) and (ack[20]==25) and (ack[22]==63) and (ack[23]==74) and (ack[24]==0) and (ack[26]==94) and (ack[27]==25) and (ack[29]==95) and running==0):
                                                                                            s.sendto(bacnetack(bvlen,npdu_c,max_apdu,invokeid,processid,obj[m],objinst,event_ack,seqn1,acksrc,stamp),(ip_address,port_no))
                                                                                            table_1.insert('', index='end',values=("Acknowledge Alarm %d"%(count),"passed"))
                                                                                            count+=1
                                                                                            tab3.update()
                                                                                            tab3.after(timedl)
                                                                                        elif(running==2): 
                                                                                            table_1.insert('', index='end',values=("Acknowledge Alarm %d"%(count),"failed"))
                                                                                            #continue
                                                                                            count+=1
                                                                                            i+=1
                                                                                        else:
                                                                                            table_1.insert('', index='end',values=("aborted"))
                                                                                            break
                                                                                else:
                                                                                    break
                                                                        else:
                                                                            break
                                                                else:
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
       
def bacnet_iam(ip_address,port_no,timedl):
    bvlen=random.randrange(24,5238)
    npdu_control=random.randrange(32,80)
    npdu_dst_mac=random.randrange(0,65536)
    npdu_dst_mac_length=random.randrange(0,256)
    npdu_hopcount=random.randrange(0,256)
    objid1=random.randrange(0,4000,64)
    objinst=random.randrange(0,65536)
    max_apdu=random.randrange(0,256)
    segment=random.randrange(0,5)
    vendorid=random.randrange(0,256)
    count=1
    
    bac_iam=bacnetiam(bvlen,npdu_control,npdu_dst_mac,npdu_dst_mac_length,npdu_hopcount,objid1,objinst,max_apdu,segment,vendorid)
    
    for bvlen in range(24,65536):
        if running==0:
            for npdu_control in range(32,80):
                if running==0:
                    for npdu_dst_mac in range(0,65536):
                        if running==0:
                            for npdu_dst_mac_length in range(0,256):
                                if running==0:
                                    for npdu_hopcount in range(0,256):
                                        if running==0:
                                            for objinst in range(0,65536):
                                                if running==0:
                                                    for max_apdu in range(0,256):
                                                        if running==0:
                                                            for segment in range(0,5):
                                                                if running==0:
                                                                    for vendorid in range(0,256):
                                                                        #response=os.system("ping -n 1 "+ip_address)
                                                                        #if response==1:
                                                                        if ((bac_iam[0]==129)and (bac_iam[1]==10) and (bac_iam[4]==1) and (bac_iam[10]==16) and (bac_iam[11]==0) and (bac_iam[12]==196) and (bac_iam[17]==34)and (bac_iam[20]==145)and (bac_iam[22]==33) and running==0):
                                                                            s.sendto(bacnetiam(bvlen,npdu_control,npdu_dst_mac,npdu_dst_mac_length,npdu_hopcount,512,objinst,max_apdu,segment,vendorid),(ip_address,port_no))                                          
                                                                            table_1.insert('', index='end',values=("I_AM %d"%(count),"passed"))                                            
                                                                            count+=1
                                                                            tab3.update()
                                                                            tab3.after(timedl)
                                                                        elif(running==2):
                                                                            table_1.insert('', index='end',values=("I_AM %d"%(count),"failed"))
                                                                            continue
                                                                            count+=1
                                                                            #i+=1
                                                                        else:
                                                                            table_1.insert('', index='end',values=("aborted"))
                                                                            break
                                                                else:
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                                
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break

def bacnet_unconfcov(ip_address,port_no,timedl,obj):
    bvlen=random.randrange(42,5238)
    npdu_control=random.randrange(0,80)
    processid=random.randrange(0,256)
    deviceid=512
    deviceinst=random.randrange(0,65536)
    objid1=random.randrange(0,4000,64)
    objinst=random.randrange(0,65536)
    propid1=random.randrange(0,256)
    propinst1=random.randrange(0,65536)
    propinst2=random.randrange(0,65536)
    propid2=random.randrange(0,256)
    propinst3=random.randrange(0,65536)
    propinst4=random.randrange(0,65536)
    count=1
    
    unconf=bacnetunconfcov(bvlen,npdu_control,processid,deviceid,deviceinst,objid1,objinst,propid1,propinst1,propinst2,propid2,propinst3,propinst4)
   
    for bvlen in range(42,5238):
        if running==0:
            for npdu_control in range(0,80):
                if running==0:
                    for processid in range(0,256):
                        if running==0:
                            for deviceinst in range(0,65536):
                                if running==0:
                                    for m in range(len(obj)):
                                        if running==0:
                                            for objinst in range(0,65536):
                                                if running==0:
                                                    for propid1 in range(0,256):
                                                        if running==0:
                                                            for propinst1 in range(0,65536):
                                                                if running==0:
                                                                    for propinst2 in range(0,65536):
                                                                        if running==0:
                                                                            for propid2 in range(0,256):
                                                                                if running==0:
                                                                                    for propinst3 in range(0,65536):
                                                                                        if running==0:
                                                                                            for propinst4 in range(0,65536):
                                                                                                #response=os.system("ping -n 1 "+ip_address)
                                                                                                if ((unconf[0]==129) and (unconf[1]==10) and (unconf[6]==16) and (unconf[7]==2) and (unconf[8]==9) and (unconf[10]==28) and (unconf[15]==44) and (unconf[20]==57) and (unconf[21]==59) and (unconf[22]==78) and (unconf[23]==9) and (unconf[25]==46) and (unconf[26]==68) and (unconf[31]==47) and (unconf[32]==9) and (unconf[35]==68) and (unconf[40]==47) and (unconf[41]==79) and running==0):
                                                                                                    s.sendto(bacnetunconfcov(bvlen,npdu_control,processid,deviceid,deviceinst,obj[m],objinst,propid1,propinst1,propinst2,propid2,propinst3,propinst4),(ip_address,port_no))
                                                                                                    table_1.insert('', index='end',values=("Unconfirmed COV %d"%(count),"passed"))
                                                                                                    tab3.update()
                                                                                                    tab3.after(timedl)
                                                                                                    count+=1
                                                                                                elif(running==2):
                                                                                                    table_1.insert('', index='end',values=("Unconfirmed_COV %d"%(count),"failed"))
                                                                                                    #continue
                                                                                                    count+=1
                                                                                                    #i+=1
                                                                                                else:
                                                                                                    table_1.insert('', index='end',values=("aborted"))
                                                                                                    break
                                                                                        else:
                                                                                            break
                                                                                else:
                                                                                    break
                                                                        else:
                                                                            break
                                                                else:
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                     break
                        else:
                            break
                else:
                    break
        else:
            break

def bacnet_unconfevent(ip_address,port_no,timedl,obj):
  bvlen=random.randrange(57,5238)
  npdu_c=0
  processid=random.randrange(0,256)
  deviceid=512
  deviceinst=random.randrange(0,65536)
  objid=random.randrange(0,4000,64)
  objinst=random.randrange(57,5238)
  sqno=random.randrange(0,256)
  notcls=random.randrange(0,256)
  pr=random.randrange(0,256)
  etype=random.randrange(0,256)
  m1=random.randrange(0,65536)
  m2=random.randrange(0,65536)
  m3=random.randrange(0,256)
  nottype=random.randrange(0,256)
  ackreq=random.randrange(0,256)
  fs=random.randrange(0,256)
  ts=random.randrange(0,256)
  bv=random.randrange(0,10)
  sf=random.randrange(0,256)
  count=1

  
  unevent=bacnetunconfevent(bvlen,npdu_c,processid,deviceid,deviceinst,objid,objinst,sqno,notcls,pr,etype,m1,m2,m3,nottype,ackreq,fs,ts,bv,sf)
  
  for bvlen in range(42,5238):
    if running==0:
        for npdu_c in range(0,80):
            if running==0:
                for processid in range(0,256):
                    if running==0:
                        for deviceinst in range(0,65536):
                            if running==0:
                                for m in range(len(obj)):
                                    if running==0:
                                        for objinst in range(0,65536):
                                            if running==0:
                                                for sqno in range(0,256):
                                                    if running==0:
                                                        for notcls in range(0,256):
                                                            if running==0:
                                                                for pr in range(0,256):
                                                                    if running==0:
                                                                        for etype in range(0,256):
                                                                            if running==0:
                                                                                for m1 in range(0,65536):
                                                                                    if running==0:
                                                                                        for m2 in range(0,65536):
                                                                                            if running==0:
                                                                                                for m3 in range(0,65536):
                                                                                                    if running==0:
                                                                                                        for nottytpe in range(0,256):
                                                                                                            if running==0:
                                                                                                                for ackreq in range(0,256):
                                                                                                                    if running==0:
                                                                                                                        for fs in range(0,256):
                                                                                                                            if running==0:
                                                                                                                                for ts in range(0,256):
                                                                                                                                    if running==0:
                                                                                                                                        for bv in range(0,256):
                                                                                                                                            if running==0:
                                                                                                                                                for sf in range(0,256):
                                                                                                                                                    if ((unevent[0]==129) and (unevent[1]==10) and (unevent[4]==1) and (unevent[6]==16) and (unevent[7]==3) and (unevent[8]==9) and (unevent[10]==28) and (unevent[15]==44) and (unevent[20]==62) and (unevent[21]==25) and (unevent[23]==63) and (unevent[24]==73) and (unevent[26]==89) and (unevent[28]==105) and (unevent[30]==125) and (unevent[31]==6) and (unevent[32]==0) and (unevent[40]==153) and (unevent[42]==169) and (unevent[44]==185) and (unevent[46]==206) and (unevent[47]==30) and (unevent[48]==14) and (unevent[49]==9) and (unevent[51]==15 and (unevent[52]==26)) and (unevent[53]==4) and (unevent[55]==31) and (unevent[56]==207) and running==0):
                                                                                                                                                        s.sendto(bacnetunconfevent(bvlen,npdu_c,processid,deviceid,deviceinst,obj[m],objinst,sqno,notcls,pr,etype,m1,m2,m3,nottype,ackreq,fs,ts,bv,sf),(ip_address,port_no))
                                                                                                                                                        table_1.insert('', index='end',values=("Unconfirmed_Event %d"%(count),"passed"))
                                                                                                                                                        tab3.update()
                                                                                                                                                        tab3.after(timedl)
                                                                                                                                                        count+=1
                                                                                                                                                    elif(running==2):
                                                                                                                                                        table_1.insert('', index='end',text="Unconfirmed_Event %d"%(count),values=("failed"))
                                                                                                                                                        #continue
                                                                                                                                                        count+=1
                                                                                                                                                        #i+=1
                                                                                                                                                    else:
                                                                                                                                                        table_1.insert('', index='end',values=("aborted"))
                                                                                                                                                        break
                                                                                                                                            else:
                                                                                                                                                break
                                                                                                                                    else:
                                                                                                                                        break
                                                                                                                            else:
                                                                                                                                break
                                                                                                                    else:
                                                                                                                        break
                                                                                                            else:
                                                                                                                break
                                                                                                    else:
                                                                                                        break
                                                                                                    
                                                                                            else:
                                                                                                break
                                                                                    else:
                                                                                        break
                                                                            else:
                                                                                break
                                                                    else:
                                                                        break
                                                            else:
                                                                break
                                                    else:
                                                        break
                                            else:
                                                break
                                    else:
                                        break
                            else:
                                break
                    else:
                        break
            else:
                break
    else:
        break

def bacnet_unconfpt(ip_address,port_no):
    s.sendto(bacnetunconfprivatet(),(ip_address,port_no))
                                                                                 
def bacnet_timesyn(ip_address,port_no,timedl):
    bvlen=random.randrange(18,5238)
    npdu_c=0
    date1=random.randrange(0,256)
    date_month=random.randrange(0,256)
    date_day=random.randrange(0,256)
    date_week=random.randrange(0,256)
    time1=random.randrange(0,256)
    time_min=random.randrange(0,256)
    time_secs=random.randrange(0,256)
    time_msecs=random.randrange(0,256)
    count=1
    
    timesyn=bacnettimesyn(bvlen,npdu_c,date1,date_month,date_day,date_week,time1,time_min,time_secs,time_msecs)
  
    for bvlen in range(18,5238):
        if running==0:
            for npdu_control in range(32,80):
                if running==0:
                    for date1 in range(0,256):
                        if running==0:
                            for date_month in range(0,256):
                                if running==0:
                                    for date_day in range(0,256):
                                        if running==0:
                                            for date_week in range(0,256):
                                                if running==0:
                                                    for time_min in range(0,256):
                                                        if running==0:
                                                            for time_secs in range(0,256):
                                                                if running==0:
                                                                    for time_msecs in range(0,256):
                                                                        #response=os.system("ping -n 1 "+ip_address)
                                                                        if ((timesyn[0]==129) and (timesyn[1]==10) and (timesyn[6]==16) and (timesyn[7]==6) and (timesyn[8]==164) and (timesyn[13]==180) and running==0):
                                                                            s.sendto(bacnettimesyn(bvlen,npdu_c,date1,date_month,date_day,date_week,time1,time_min,time_secs,time_msecs),(ip_address,port_no))
                                                                            time.sleep(0.1)
                                                                            table_1.insert('', index='end',values=("Time_Synchronization %d"%(count),"passed"))
                                                                            count+=1
                                                                            tab3.update()
                                                                            tab3.after(timedl)
                                                                        elif(running==2):
                                                                            table_1.insert('', index='end',values=("Time_Synchronization %d"%(count),"failed"))
                                                                            continue
                                                                            count+=1
                                                                        else:
                                                                            table_1.insert('', index='end',values=("aborted"))
                                                                            break
                                                                else:
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
    
def bacnet_utctimesyn(ip_address,port_no,timedl):
    bvlen=random.randrange(18,65536)
    npdu_c=0
    date1=random.randrange(0,256)
    date_month=random.randrange(0,256)
    date_day=random.randrange(0,256)
    date_week=random.randrange(0,256)
    time1=random.randrange(0,256)
    time_min=random.randrange(0,256)
    time_secs=random.randrange(0,256)
    time_msecs=random.randrange(0,256)
    count=1
 
    utcsyn=bacnetutctimesyn(bvlen,npdu_c,date1,date_month,date_day,date_week,time1,time_min,time_secs,time_msecs)
   
    for bvlen in range(18,65536):
        if running==0:
            for npdu_control in range(32,80):
                if running==0:
                    for date1 in range(0,256):
                        if running==0:
                            for date_month in range(0,256):
                                if running==0:
                                    for date_day in range(0,256):
                                        if running==0:
                                            for date_week in range(0,256):
                                                if running==0:
                                                    for time_min in range(0,256):
                                                        if running==0:
                                                            for time_secs in range(0,256):
                                                                if running==0:
                                                                    for time_msecs in range(0,256):
                                                                        #response=os.system("ping -n 1 "+ip_address)
                                                                        if ((utcsyn[0]==129) and (utcsyn[1]==10) and (utcsyn[6]==16) and (utcsyn[7]==9) and (utcsyn[8]==164) and (utcsyn[13]==180) and running==0):
                                                                            s.sendto(bacnetutctimesyn(bvlen,npdu_c,date1,date_month,date_day,date_week,time1,time_min,time_secs,time_msecs),(ip_address,port_no))                                       
                                                                            #print("Task %d"%(count))
                                                                            table_1.insert('', index='end',values=("UTC_TimeSynchronization %d"%(count),"passed"))
                                                                            count+=1
                                                                            tab3.after(timedl)
                                                                            tab3.update()
                                                                        elif(running==2):
                                                                            table_1.insert('', index='end',values=("UTC_TimeSynchronization %d"%(count),"failed"))
                                                                            continue
                                                                            count+=1
                                                                        else:
                                                                            table_1.insert('', index='end',values=("aborted"))
                                                                            break
                                                                else:
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
                                                                                                                  
def bacnet_whohas(ip_address,port_no,timedl,obj):
    bvlen=random.randrange(23,5238)
    npdu_control=random.randrange(32,80)
    dst_mac=random.randrange(0,65536)
    dst_mac_length=random.randrange(0,256)
    hop_count=random.randrange(0,256)
    device_lowlimit=random.randrange(0,65536)
    device_highlimit=random.randrange(0,65536)
    objid1=random.randrange(0,4000,64)
    objinst=random.randrange(0,65536)
    count=1
    
    who_has=bacnetwhohas(bvlen,npdu_control,dst_mac,dst_mac_length,hop_count,device_lowlimit,device_highlimit,objid1,objinst)
   
    for bvlen in range(23,5238):
        if running==0:
            for npdu_control in range(32,80):
                if running==0:
                    for dst_mac in range(0,65536):
                        if running==0:
                            for dst_mac_length in range(0,256): 
                                if running==0:
                                    for hop_count in range(0,256): 
                                        if running==0:
                                            for device_lowlimit in range(0,65536): 
                                                if running==0:
                                                    for device_highlimit in range(0,65536):
                                                        if running==0:
                                                            for m in range(len(obj)): 
                                                                if running==0:
                                                                    for objinst in range(0,65536):
                                                                        if ((who_has[0]==129) and(who_has[1]==11) and (who_has[4]==1) and (who_has[10]==16) and (who_has[11]==7) and (who_has[12]==10) and (who_has[15]==26) and (who_has[18]==44) and running==0):
                                                                            s.sendto(bacnetwhohas(bvlen,npdu_control,dst_mac,dst_mac_length,hop_count,device_lowlimit,device_highlimit,obj[m],objinst),(ip_address,port_no))
                                                                            table_1.insert('', index='end',values=("Who_Has %d"%(count),"passed"))
                                                                            count+=1
                                                                            tab3.update()
                                                                            t=tab3.after(timedl)
                                                                        elif(running==2):
                                                                            table_1.insert('', index='end',values=("Who_Has %d"%(count),"failed"))
                                                                            continue
                                                                            count+=1
                                                                            i+=1
                                                                        else:
                                                                            table_1.insert('', index='end',values=("aborted"))
                                                                            break
                                                                else:
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
                                       
def bacnet_whois(ip_address,port_no,timedl):
    
    bvlen=random.randrange(22,5238)
    npdu_control=random.randrange(32,80)
    npdu_dst_mac=random.randrange(0,65536)
    npdu_dst_mac_length=random.randrange(0,256)
    npdu_hopcount=random.randrange(0,256)
    #device_lowlimit1=random.randrange(0,65536)
    device_lowlimit2=random.randrange(0,65536)
    #device_highlimit1=random.randrange(0,65536)
    device_highlimit2=random.randrange(0,65536)
    count=1
    
    whois=bacnetwhois(bvlen,npdu_control,npdu_dst_mac,npdu_dst_mac_length,npdu_hopcount,device_lowlimit2,device_highlimit2)
   
    for bvlen in range(22,65536):
        if running==0:
            for npdu_control in range(32,80):
                if running==0:
                    for npdu_dst_mac in range(0,65536):
                        if running==0:
                            for npdu_dst_mac_length in range(0,256):
                                if running==0:
                                    for npdu_hopcount in range(0,256):
                                        if running==0:
                                            for device_lowlimit2 in range(0,65536):
                                                if running==0:
                                                    for device_highlimit2 in range(0,65536):
                                                        #response=os.system("ping -n 1 "+ip_address)
                                                            if ((whois[0]==129) and(whois[4]==1) and (whois[10]==16) and (whois[11]==8) and (whois[12]==12) and (whois[17]==28) and running==0):
                                                                #print('valid packet')
                                                                s.sendto(bacnetwhois(bvlen,npdu_control,npdu_dst_mac,npdu_dst_mac_length,npdu_hopcount,device_lowlimit2,device_highlimit2),(ip_address, port_no))
                                                                table_1.insert('', index='end',values=("Who_Is %d"%(count),"passed"))                                
                                                                count+=1
                                                                tab3.update()
                                                                t=tab3.after(timedl)
                                                            elif(running==2):
                                                                table_1.insert('', index='end',values=("Who_Is %d"%(count),"failed"))
                                                                continue
                                                                count+=1
                                                                i+=1
                                                            else:   
                                                                table_1.insert('', index='end',values=("aborted"))
                                                                break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break

def bacnet_concov(ip_address,port_no,timedl,obj):
    bvlen=random.randrange(44,5238)
    npdu_control=4
    processid=random.randrange(0,256)
    deviceid=512
    deviceinst=random.randrange(0,65536)
    objid1=random.randrange(0,4000,64)
    objinst=random.randrange(0,65536)
    propid1=random.randrange(0,256)
    propinst1=random.randrange(0,65536)
    propinst2=random.randrange(0,65536)
    propid2=random.randrange(0,256)
    propinst3=random.randrange(0,65536)
    propinst4=random.randrange(0,65536)
    count=1
   
    
    confcov=bacnetconfcov(bvlen,npdu_control,processid,deviceid,deviceinst,objid1,objinst,propid1,propinst1,propinst2,propid2,propinst3,propinst4)
    
    for bvlen in range(44,5238):
        if running==0:
            for npdu_control in range(0,80):
                if running==0:
                    for processid in range(0,256):
                        if running==0:
                            for deviceinst in range(len(obj)):
                                if running==0:
                                    for m in range(0,4000,64):
                                        if running==0:
                                            for objinst in range(0,65536):
                                                if running==0:
                                                    for propid1 in range(0,256):
                                                        if running==0:
                                                            for propinst1 in range(0,65536):
                                                                if running==0:
                                                                    for propinst2 in range(0,65536):
                                                                        if running==0:
                                                                            for propid2 in range(0,256):
                                                                                if running==0:
                                                                                    for propinst3 in range(0,65536):
                                                                                        if running==0:
                                                                                            for propinst4 in range(0,65536):
                                                                                                #response=os.system("ping -n 1 "+ip_address)
                                                                                                if ((confcov[0]==129) and (confcov[1]==10) and (confcov[6]==0) and (confcov[7]==3) and (confcov[8]==75) and (confcov[9]==1) and (confcov[10]==9) and (confcov[12]==28) and (confcov[17]==44) and (confcov[22]==57) and (confcov[23]==59) and (confcov[24]==78) and (confcov[25]==9) and (confcov[27]==46) and (confcov[28]==68) and (confcov[33]==47) and (confcov[34]==9) and (confcov[36]==46) and (confcov[37]==68) and (confcov[42]==47) and (confcov[43]==79) and running==0):
                                                                                                    s.sendto(bacnetconfcov(bvlen,npdu_control,processid,deviceid,deviceinst,obj[m],objinst,propid1,propinst1,propinst2,propid2,propinst3,propinst4),(ip_address,port_no))
                                                                                                    table_1.insert('', index='end',values=("Confirmed_COV %d"%(count),"passed"))
                                                                                                    tab3.update()
                                                                                                    t=tab3.after(timedl)
                                                                                                    count+=1
                                                                                                elif(running==2):
                                                                                                    table_1.insert('', index='end',text="Confirmed_COV %d"%(count),values=("failed"))
                                                                                                    continue
                                                                                                    count+=1
                                                                                                    i+=1 
                                                                                                else:
                                                                                                    table_1.insert('', index='end',text="Confirmed_COV %d"%(count),values=("aborted"))
                                                                                                    break
                                                                                        else:
                                                                                            break
                                                                                else:
                                                                                    break
                                                                        else:
                                                                            break
                                                                else:
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break

def bacnet_confevent(ip_address,port_no,timedl,obj):
  
  bvlen=random.randrange(59,5238)
  npdu_c=4
  processid=random.randrange(0,256)
  deviceid=512
  deviceinst=random.randrange(0,65536)
  objid=random.randrange(0,4000,64)
  objinst=random.randrange(57,5238)
  sqno=random.randrange(0,256)
  notcls=random.randrange(0,256)
  pr=random.randrange(0,256)
  etype=random.randrange(0,256)
  m1=random.randrange(0,65536)
  m2=random.randrange(0,65536)
  m3=random.randrange(0,256)
  nottype=random.randrange(0,256)
  ackreq=random.randrange(0,256)
  fs=random.randrange(0,256)
  ts=random.randrange(0,256)
  bv=random.randrange(0,10)
  sf=random.randrange(0,256)
  count=1
 
  confevent=bacnetconfevent(bvlen,npdu_c,processid,deviceid,deviceinst,objid,objinst,sqno,notcls,pr,etype,m1,m2,m3,nottype,ackreq,fs,ts,bv,sf)
  
  for bvlen in range(59,5238):
    if running==0:
        for npdu_c in range(0,80):
            if running==0:
                for processid in range(0,256):
                    if running==0:
                        for deviceinst in range(0,65536):
                            if running==0:
                                for m in range(len(obj)):
                                    if running==0:
                                        for objinst in range(0,65536):
                                            if running==0:
                                                for sqno in range(0,256):
                                                    if running==0:
                                                        for notcls in range(0,256):
                                                            if running==0:
                                                                for pr in range(0,256):
                                                                    if running==0:
                                                                        for etype in range(0,256):
                                                                            if running==0:
                                                                                for m1 in range(0,65536):
                                                                                    if running==0:
                                                                                        for m2 in range(0,65536):
                                                                                            if running==0:
                                                                                                for m3 in range(0,65536):
                                                                                                    if running==0:
                                                                                                        for nottytpe in range(0,256):
                                                                                                            if running==0:
                                                                                                                for ackreq in range(0,256):
                                                                                                                    if running==0:
                                                                                                                        for fs in range(0,256):
                                                                                                                            if running==0:
                                                                                                                                for ts in range(0,256):
                                                                                                                                    if running==0:
                                                                                                                                        for bv in range(0,256):
                                                                                                                                            if running==0:
                                                                                                                                                for sf in range(0,256):
                                                                                                                                                    if ((confevent[0]==129) and (confevent[1]==10) and (confevent[4]==1) and (confevent[6]==0) and (confevent[9]==2) and (confevent[10]==9) and (confevent[12]==28) and (confevent[17]==44) and (confevent[22]==62) and (confevent[23]==25) and (confevent[25]==63) and (confevent[26]==73) and (confevent[28]==89) and (confevent[30]==105) and (confevent[32]==125) and (confevent[33]==6) and (confevent[34]==0) and (confevent[42]==153) and (confevent[44]==169) and (confevent[46]==185) and (confevent[48]==206) and (confevent[49]==30) and (confevent[50]==14) and (confevent[51]==9) and (confevent[53]==15) and (confevent[54]==26) and (confevent[55]==4) and (confevent[57]==31) and (confevent[58]==207) and running==0):
                                                                                                                                                        s.sendto(bacnetconfevent(bvlen,npdu_c,processid,deviceid,deviceinst,obj[m],objinst,sqno,notcls,pr,etype,m1,m2,m3,nottype,ackreq,fs,ts,bv,sf),(ip_address,port_no))
                                                                                                                                                        table_1.insert('', index='end',values=("Confirmed_Event %d"%(count),"passed"))
                                                                                                                                                        tab3.update()
                                                                                                                                                        t=tab3.after(timedl)
                                                                                                                                                        count+=1
                                                                                                                                                    elif(running==2):
                                                                                                                                                        table_1.insert('', index='end',values=("Confirmed_Event %d"%(count),"failed"))
                                                                                                                                                        continue
                                                                                                                                                        count+=1
                                                                                                                                                        i+=1
                                                                                                                                                    else:
                                                                                                                                                        table_1.insert('', index='end',values=("aborted"))
                                                                                                                                                        break
                                                                                                                                            else:
                                                                                                                                                break
                                                                                                                                    else:
                                                                                                                                        break
                                                                                                                            else:
                                                                                                                                break
                                                                                                                    else:
                                                                                                                        break
                                                                                                            else:
                                                                                                                break
                                                                                                    else:
                                                                                                        break
                                                                                            else:
                                                                                                break
                                                                                    else:
                                                                                        break
                                                                            else:
                                                                                break
                                                                    else:
                                                                        break
                                                                     
                                                    else:
                                                        break
                                            else:
                                                break
                                    else:
                                        break
                            else:
                                break
                    else:
                        break
            else:
                break
    else:
        break

def bacnet_confpt(ip_address,port_no):
    s.sendto(bacnetconfprivatet(),(ip_address,port_no))
    
def bacnet_alarm(ip_address,port_no,timedl):
    
    bvlen=random.randrange(10,5238)
    npdu_control=4
    max_apdu=random.randrange(0,256)
    invoke_id=random.randrange(0,256)
    count=1
    
    bac_alarm=Bacnetalarm(bvlen,npdu_control,max_apdu,invoke_id)
    
    
    for bvlen in range(10,5238):
        if running==0:
            for npdu_cntrl in range(0,80):
                if running==0:
                    for max_apdusz in range(0,256):
                        if running==0:
                            for invoke_id in range(0,256):
                                    if ((bac_alarm[0]==129) and (bac_alarm[1]==10) and (bac_alarm[4]==1) and (bac_alarm[6]==0) and (bac_alarm[9]==3) and running==0):
                                        s.sendto(Bacnetalarm(bvlen,npdu_control,max_apdu,invoke_id),(ip_address,port_no))
                                        table_1.insert('', index='end',values=("Alarm Summary %d"%(count),"passed"))
                                        count+=1
                                        tab3.update()
                                        tab3.after(timedl)
                                    elif(running==2):
                                        table_1.insert('', index='end',values=("Alarm Summary %d"%(count),"failed"))
                                        continue
                                        count+=1
                                    else:
                                        table_1.insert('', index='end',values=("aborted"))
                                        break
                        else:
                            break
                else:
                    break
        else:
            break
  
def bacnet_enroll(ip_address,port_no,timedl):
    
    bvlen=random.randrange(4,65536)
    npdu_control=4
    max_apdu=random.randrange(0,256)
    invoke_id=random.randrange(0,256)
    ackft=2304
    rece_objid=512
    rece_objinst=random.randrange(0,65536)
    process_id=random.randrange(6400,6656)
    stateft=random.randrange(0,5)
    typeft=random.randrange(0,256)
    count=1
    
    enr=bacnetenroll(bvlen,npdu_control,max_apdu,invoke_id,ackft,rece_objid,rece_objinst,process_id,stateft,typeft)
    
    for bvlen in range(27,65536):
        if running==0:
            for npdu_cntrl in range(0,80):
                if running==0:
                    for max_apdusz in range(0,256):
                        if running==0:
                            for invoke_id in range(0,256):
                                if running==0:
                                    for process_id in range(6400,6656):
                                        if running==0:
                                            for rece_objinst in range(0,256):
                                                if running==0:
                                                    for stateft in range(0,5):
                                                        if running==0:
                                                            for typeft in range(0,256):
                                                                if ((enr[0]==129) and (enr[1]==10) and (enr[4]==1) and (enr[6]==0) and (enr[9]==4) and (enr[12]==30) and (enr[13]==14) and (enr[14]==12) and (enr[19]==15) and (enr[22]==31) and (enr[25]==57) and running==0):
                                                                    s.sendto(bacnetenroll(bvlen,npdu_control,max_apdu,invoke_id,ackft,rece_objid,rece_objinst,process_id,stateft,typeft),(ip_address,port_no))
                                                                    table_1.insert('', index='end',values=("Enrollment Summary %d"%(count),"passed"))
                                                                    count+=1
                                                                    tab3.after(timedl)
                                                                    tab3.update()
                                                                    count+=1
                                                                elif(running==2):
                                                                    table_1.insert('', index='end',values=("Enrollment Summary %d"%(count),"failed"))
                                                                    continue
                                                                    count+=1
                                                                else:
                                                                    table_1.insert('', index='end',values=("aborted"))
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
                                        
def bacnet_cov(ip_address,port_no,timedl,obj):
    bvlen=random.randrange(22,5238)
    npdu_control=4
    max_apdu=random.randrange(0,256)
    invoke_id=random.randrange(0,256)
    sub_processid=random.randrange(0,256)
    objectid1=random.randrange(0,4000,64)
    objinst=random.randrange(0,65536)
    issue_notif=random.randrange(0,256)
    context3=random.choice([57,58])
    lifetime=random.randrange(0,65536)
    count=1
    
    cov=bacnetcov(bvlen,npdu_control,max_apdu,invoke_id,sub_processid,objectid1,objinst,issue_notif,context3,lifetime)
    
    for bvlen in range(22,5238):
        if running==0:
            for npdu_control in range(0,80):
                if running==0:
                    for max_apdu in range(0,256):
                        if running==0:
                            for invoke_id in range(0,256):
                                if running==0:
                                    for subscriber_processid in range(0,256):
                                        if running==0:
                                            for m in range(len(obj)):
                                                if running==0:
                                                    for objinst in range(0,256):
                                                        if running==0:
                                                            for issue_notification in range(0,256):
                                                                if running==0:
                                                                    for lifetime in range(0,65536):                                        
                                                                            if ((cov[0]==129) and (cov[1]==10) and (cov[4]==1) and (cov[6]==0) and (cov[9]==5) and (cov[10]==9) and (cov[12]==28) and (cov[17]==41) and (cov[19]==57 or cov[19]==58) and running==0):
                                                                                s.sendto(bacnetcov(bvlen,npdu_control,max_apdu,invoke_id,sub_processid,obj[m],objinst,issue_notif,context3,lifetime),(ip_address,port_no))
                                                                                table_1.insert('', index='end',values=("Subscribe_COV %d"%(count),"passed"))
                                                                                count+=1
                                                                                tab3.update()
                                                                                tab3.after(timedl)                                                                                
                                                                            elif(running==2):  
                                                                                table_1.insert('', index='end',values=("Subscribe_COV %d"%(count),"failed"))
                                                                                continue
                                                                                count+=1
                                                                            else:
                                                                                table_1.insert('', index='end',values=("aborted"))
                                                                                break
                                                                else:
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
    
def bacnet_readfile(ip_address,port_no,timedl,obj):
    bvlen=random.randrange(0,5238)
    npdu_control=random.randrange(0,80)
    max_apdu=random.randrange(0,256)
    invoke_id=random.randrange(0,256)
    objid1=random.randrange(0,4000,64)
    objinst=random.randrange(0,65536)
    startrec=random.randrange(0,256)
    reqcount=random.randrange(0,256)
    count=1
    
    readf=bacnetreadfile(bvlen,npdu_control,max_apdu,invoke_id,objid1,objinst,startrec,reqcount)
    
    for bvlen in range(21,5238):
        if running==0:
            for npdu_control in range(0,80):
                if running==0:
                    for max_apdu in range(0,256):
                        if running==0:
                            for invoke_id in range(0,256):
                                if running==0:
                                    for m in range(len(obj)):
                                        if running==0:
                                            for objinst in range(0,65536):
                                                if running==0:
                                                    for startrec in range(0,256):
                                                        if running==0:
                                                            for reqcount in range(0,256):
                                                                if ((readf[0]==129) and (readf[1]==10) and (readf[4]==1) and (readf[6]==0) and (readf[9]==6) and (readf[10]==12) and (readf[15]==14) and (readf[16]==49) and (readf[18]==33) and (readf[20]==15) and running==0):
                                                                    s.sendto(bacnetreadfile(bvlen,npdu_control,max_apdu,invoke_id,obj[m],objinst,startrec,reqcount),(ip_address,port_no))
                                                                    table_1.insert('', index='end',values=("Read_File %d"%(count),"passed"))
                                                                    tab3.update()
                                                                    time.sleep(0.1)
                                                                    count+=1
                                                                elif(running==2):
                                                                    table_1.insert('', index='end',text="Read_File %d"%(count),values=("failed"))
                                                                    continue
                                                                    count+=1
                                                                    i+=1
                                                                else:
                                                                    table_1.insert('', index='end',values=("aborted"))
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
                                           
def bacnet_writefile(ip_address,port_no,timedl,obj):
    bvlen=random.randrange(0,5238)
    npdu_control=random.randrange(0,80)
    max_apdu=random.randrange(0,256)
    invoke_id=random.randrange(0,256)
    objid1=random.randrange(0,4000,64)
    objinst=random.randrange(0,65536)
    startrec=random.randrange(0,256)
    reqcount=random.randrange(0,256)
    count=1
   
    writef=bacnetwritefile(bvlen,npdu_control,max_apdu,invoke_id,objid1,objinst,startrec,reqcount)
    
    for bvlen in range(21,5238):
        if running==0:
            for npdu_control in range(0,80):
                if running==0:
                    for max_apdu in range(0,256):
                        if running==0:
                            for invoke_id in range(0,256):
                                if running==0:
                                    for m in range(len(obj)):
                                        if running==0:
                                            for objinst in range(0,256):
                                                if running==0:
                                                    for startrec in range(0,256):
                                                        if running==0:
                                                            for reqcount in range(0,256):
                                                                if ((writef[0]==129) and (writef[1]==10) and (writef[4]==1) and (writef[6]==0) and (writef[9]==7) and (writef[10]==12) and (writef[15]==14) and (writef[16]==49) and (writef[18]==33) and (writef[20]==15) and running==0):
                                                                    s.sendto(bacnetwritefile(bvlen,npdu_control,max_apdu,invoke_id,obj[m],objinst,startrec,reqcount),(ip_address,port_no))
                                                                    table_1.insert('', index='end',values=("WriteFile %d"%(count),"passed"))
                                                                    tab3.update()
                                                                    tab3.after(timedl)
                                                                    count+=1                                                                  
                                                                elif(running==2):
                                                                    table_1.insert('', index='end',text="WriteFiel %d"%(count),values=("failed"))
                                                                    continue
                                                                    count+=1
                                                                    i+=1
                                                                else:
                                                                    table_1.insert('', index='end',values=("aborted"))
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
                                                                                                                      
def bacnet_addlist(ip_address,port_no,timedl,obj):
    bvlen=random.randrange(24,5238)
    npdu_control=4
    max_apdu=random.randrange(0,256)
    invoke_id=random.randrange(0,256)
    objid1=random.randrange(0,4000,64)
    objinst=random.randrange(0,256)
    propid=random.randrange(0,256)
    prop1=random.randrange(16526,65536,128)
    prop2=random.randrange(0,65536)
    count=1

    addl=bacnetaddlist(bvlen,npdu_control,max_apdu,invoke_id,objid1,objinst,propid,prop1,prop2)
    for bvlen in range(24,5238):
        if running==0:
            for npdu_control in range(0,80):
                if running==0:
                    for max_apdu in range(0,256):
                        if running==0:
                            for invoke_id in range(0,256):
                                if running==0:
                                    for m in range(len(obj)):
                                        if running==0:
                                            for objinst in range(0,65536):
                                                if running==0:
                                                    for propid in range(0,256):
                                                        if running==0:
                                                            for prop1 in range(16526,65536,128):
                                                                if running==0:
                                                                    for prop2 in range(0,65536):
                                                                        
                                                                            if ((addl[0]==129) and (addl[1]==10) and (addl[4]==1) and (addl[6]==0) and (addl[9]==8) and (addl[10]==12) and (addl[15]==25) and (addl[17]==62) and (addl[18]==68) and (addl[23]==63) and running==0):
                                                                                s.sendto(bacnetaddlist(bvlen,npdu_control,max_apdu,invoke_id,obj[m],objinst,propid,prop1,prop2),(ip_address,port_no))
                                                                                table_1.insert('', index='end',values=("Add_List %d"%(count),"passed"))
                                                                                tab3.update()
                                                                                tab3.after(timedl)
                                                                                count+=1
                                                                            elif running==2:
                                                                                table_1.insert('', index='end',text="Add_List %d"%(count),values=("failed"))
                                                                                continue
                                                                                count+=1
                                                                                i+=1
                                                                            else:
                                                                                table_1.insert('', index='end',text="Add_List %d"%(count),values=("aborted"))
                                                                                break
                                                                else:
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
                                                                                              
def bacnet_removelist(ip_address,port_no,timedl,obj):
    
    bvlen=random.randrange(0,5238)
    npdu_control=random.randrange(0,80)
    max_apdu=random.randrange(0,256)
    invoke_id=random.randrange(0,256)
    objid1=random.randrange(0,4000,64)
    objinst=random.randrange(0,256)
    propid=random.randrange(0,256)
    prop1=random.randrange(16526,65536,128)
    prop2=random.randrange(0,65536)
    count=1

    rmvl=bacnetremovelist(bvlen,npdu_control,max_apdu,invoke_id,objid1,objinst,propid,prop1,prop2)   
    for bvlen in range(16,65536):
        if running==0:
            for npdu_control in range(0,256):
                if running==0:
                    for max_apdu in range(0,256):
                        if running==0:
                            for invoke_id in range(0,256):
                                if running==0:
                                    for m in range(len(obj)):
                                        if running==0:
                                            for objinst in range(0,65536):
                                                if running==0:
                                                    for propid in range(0,256):
                                                        if running==0:
                                                            for prop1 in range(16526,65536,128):
                                                                if running==0:
                                                                    for prop2 in range(0,65536):
                                                                        #response=os.system("ping -n 1 "+ip_address)
                                                                        if ((rmvl[0]==129) and (rmvl[1]==10) and (rmvl[4]==1) and (rmvl[6]==0) and (rmvl[9]==9) and (rmvl[10]==12) and (rmvl[15]==25) and (rmvl[17]==62) and (rmvl[18]==68) and (rmvl[23]==63) and running==0):
                                                                            s.sendto(bacnetremovelist(bvlen,npdu_control,max_apdu,invoke_id,obj[m],objinst,propid,prop1,prop2),(ip_address,port_no))
                                                                            table_1.insert('', index='end',values=("Remove_List %d"%(count),"passed"))
                                                                            tab3.update()
                                                                            tab3.after(timedl)
                                                                            count+=1
                                                                        elif(running==2):
                                                                            table_1.insert('', index='end',text="Remove_List %d"%(count),values=("failed"))
                                                                            continue
                                                                            count+=1
                                                                            i+=1
                                                                        else:
                                                                            table_1.insert('', index='end',values=("aborted"))
                                                                            break
                                                                else:
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
                                           
def bacnet_create(ip_address,port_no,timedl,obj):
    bvlen=random.randrange(0,5238)
    npdu_control=4
    max_apdu=random.randrange(0,80)
    invoke_id=random.randrange(0,256)
    objectid1=random.randrange(0,4000,64)
    objectinst=random.randrange(0,65536)
    propid=random.randrange(0,256)
    count=1
    
    bac_create=bacnetcreate(bvlen,npdu_control,max_apdu,invoke_id,objectid1,objectinst,propid)
    
    for bvlen in range(16,5238):
        if running==0:
            for npdu_control in range(0,80):
                if running==0:
                    for max_apdu in range(0,256):
                        if running==0:
                            for invoke_id in range(0,256):
                                if running==0:
                                    for m in range(len(obj)):
                                        if running==0:
                                            for objectinst in range(0,256):
                                                if running==0:
                                                    for propid in range(0,256):
                                                        #response=os.system("ping -n 1 "+ip_address)
                                                        #if response==1:
                                                        if ((bac_create[0]==129) and(bac_create[1]==10) and (bac_create[4]==1) and (bac_create[6]==0) and (bac_create[9]==10) and (bac_create[10]==14) and (bac_create[11]==28) and (bac_create[16]==15) and (bac_create[17]==39) and (bac_create[18]==9) and (bac_create[20]==46) and (bac_create[21]==47) and (bac_create[22]==31) and running==0):
                                                            s.sendto(bacnetcreate(bvlen,npdu_control,max_apdu,invoke_id,obj[m],objectinst,propid),(ip_address,port_no))
                                                            table_1.insert('', index='end',values=("Create_object %d"%(count),"passed"))
                                                            tab3.update()
                                                            tab3.after(timedl)
                                                            count+=1
                                                        elif(running==2):
                                                            table_1.insert('', index='end',values=("Create_object %d"%(count),"failed"))
                                                            continue
                                                            count+=1
                                                            i+=1
                                                        else:
                                                            table_1.insert('', index='end',values=("aborted"))
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break

def bacnet_delete(ip_address,port_no,timedl,obj):

    bvlen=random.randrange(0,5238)
    npdu_control=4
    max_apdu=random.randrange(0,80)
    invoke_id=random.randrange(0,256)
    objectid1=random.randrange(0,4000,64)
    objectinst1=random.randrange(0,65536)
    count=1
    
    bac_delete=bacnetdelete(bvlen,npdu_control,max_apdu,invoke_id,objectid1,objectinst1)
   
    for bvlen in range(16,65536):
        if running==0:
            for npdu_control in range(0,80):
                if running==0:
                    for max_apdu in range(0,256):
                        if running==0:
                            for invoke_id in range(0,256):
                                if running==0:
                                    for m in range(len(obj)):
                                        if running==0:
                                            for objectinst in range(0,256):
                                                #response=os.system("ping -n 1 "+ip_address)
                                                #if response==1:
                                                if ((bac_delete[0]==129) and (bac_delete[1]==10) and (bac_delete[4]==1) and (bac_delete[6]==0) and (bac_delete[9]==11) and (bac_delete[10]==196) and running==0):
                                                    s.sendto(bacnetdelete(bvlen,npdu_control,max_apdu,invoke_id,obj[m],objectinst), (ip_address, port_no))
                                                    table_1.insert('', index='end',values=("DeleteObject %d"%(count),"passed"))
                                                    tab3.update()
                                                    tab3.after(timedl)
                                                    count+=1
                                                elif(running==2):    
                                                    table_1.insert('', index='end',values=("DeleteObject %d"%(count),"failed"))
                                                    continue
                                                    count+=1
                                                    i+=1
                                                else:
                                                    table_1.insert('', index='end',values=("aborted"))
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break

def bacnet_readrange(ip_address,port_no,timedl,obj):
    
    bvlen=random.randrange(0,5238)
    npdu_control=random.randrange(0,80)
    max_apdu=random.randrange(0,256)
    invoke_id=random.randrange(0,256)
    objid1=random.randrange(0,4000,64)
    objinst=random.randrange(0,65536)
    propid=random.randrange(0,256)
    ref_in=random.randrange(0,256)
    ref_count=random.randrange(0,256)
    range1=random.choice([62,110,126])
    range2=range1+1
    count=1

    readrn=bacnetreadrange(bvlen,npdu_control,max_apdu,invoke_id,objid1,objinst,propid,range1,ref_in,ref_count,range2)
    
    for bvlen in range(23,65536):
        if running==0:
            for npdu_control in range(0,80):
                if running==0:
                    for max_apdu in range(0,256):
                        if running==0:
                            for invoke_id in range(0,256):
                                if running==0:
                                    for m in range(len(obj)):
                                        if running==0:
                                            for objinst in range(0,65536):
                                                if running==0:
                                                    for propid in range(0,256):
                                                        if running==0:
                                                            for ref_in in range(0,256):
                                                                if running==0:
                                                                    for ref_count in range(0,256):
                                                                        if ((readrn[0]==129) and (readrn[1]==10) and (readrn[4]==1) and (readrn[6]==0) and (readrn[9]==26) and (readrn[10]==12) and (readrn[15]==25) and (readrn[18]==33) and (readrn[20]==49) and running==0):
                                                                            s.sendto(bacnetreadrange(bvlen,npdu_control,max_apdu,invoke_id,obj[m],objinst,propid,range1,ref_in,ref_count,range2),(ip_address,port_no))
                                                                            table_1.insert('', index='end',values=("Read_Range %d"%(count),"passed"))
                                                                            tab3.update()
                                                                            tab3.after(timedl)
                                                                            count+=1
                                                                        elif(running==2):
                                                                            table_1.insert('', index='end',text="Read_Range %d"%(count),values=("failed"))
                                                                            continue
                                                                            count+=1
                                                                            i+=1
                                                                        else:
                                                                            table_1.insert('', index='end',values=("aborted"))
                                                                            break
                                                                else:
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
                                                                                        
def bacnet_read(ip_address,port_no,timedl,obj):
    
    bvlen=random.randrange(17,5238)
    npdu_control=4
    max_apdu=random.randrange(0,80)
    invoke_id=random.randrange(0,256)
    objectid1=random.randrange(0,4000,64)
    objectinst=random.randrange(0,256)
    propid1=random.randrange(0,256)
    count=1

    readp=bacnetread(bvlen,npdu_control,max_apdu,invoke_id,objectid1,objectinst,propid1)
  
    for bvlen in range(17,5238):
        if running==0:
            for npdu_control in range(0,80):
                if running==0:
                    for max_apdu in range(0,256):
                        if running==0:
                            for invoke_id in range(0,256):
                                if running==0:
                                    for m in range(len(obj)):
                                        if running==0:
                                            for objectinst in range(0,256):
                                                if running==0:
                                                    for propid1 in range(0,256):
                                                        if ((readp[0]==129) and (readp[1]==10) and (readp[4]==1) and (readp[6]==0) and (readp[9]==12) and (readp[10]==12) and (readp[15]==25) and running==0):
                                                            s.sendto(bacnetread(bvlen,npdu_control,max_apdu,invoke_id,obj[m],objectinst,propid1),(ip_address, port_no))
                                                            table_1.insert('', index='end',values=("ReadProperty %d"%(count),"passed"))
                                                            tab3.update()
                                                            tab3.after(timedl)
                                                            count+=1
                                                        elif(running==2):
                                                            table_1.insert('', index='end',text="ReadProperty %d"%(count),values=("failed"))
                                                            continue
                                                            count+=1
                                                            i+=1
                                                            
                                                        else:
                                                            table_1.insert('', index='end',values=("aborted"))
                                                            break
                                                else:    
                                                    break 
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
    
                               
def bacnet_readmultiple(ip_address,port_no,timedl,obj):
    bvlen=random.randrange(23,5238)
    npdu_control=4
    max_apdu=random.randrange(0,80)
    invoke_id=random.randrange(0,256)
    objectid1=random.randrange(0,4000,64)
    objectinst=random.randrange(0,65536)
    propid1=random.randrange(0,256)
    propid2=random.randrange(0,256)
    propid3=random.randrange(0,256)
    count=1
   
    readM=bacnetreadmultiple(bvlen,npdu_control,max_apdu,invoke_id,objectid1,objectinst,propid1,propid2,propid3)
    
    for bvlen in range(23,5238):
        if running==0:
            for npdu_control in range(0,80):
                if running==0:
                    for max_apdu in range(0,256):
                        if running==0:
                            for invoke_id in range(0,256):
                                if running==0:
                                    for m in range(len(obj)):
                                        if running==0:
                                            for objectinst in range(0,256):
                                                if running==0:
                                                    for propid1 in range(0,256):
                                                        if running==0:
                                                            for propid2 in range(0,256):
                                                                if running==0:
                                                                    for propid3 in range(0,256):
                                                                        if ((readM[0]==129) and(readM[1]==10) and (readM[4]==1) and (readM[6]==0) and (readM[9]==14) and (readM[10]==12) and (readM[15]==30) and (readM[16]==9) and (readM[18]==9) and (readM[20]==9) and (readM[22]==31) and running==0):
                                                                            s.sendto(bacnetReadMultiple(bvlen,npdu_control,max_apdu,invoke_id,obj[m],objectinst,propid1,propid2,propid3), (ip_address,port_no))
                                                                            #ws.after(timed)
                                                                            time.sleep(0.1)
                                                                            table_1.insert('', index='end',values=("ReadProperty_Multiple%d"%(count),"passed"))
                                                                            t=tab3.after(timedl)
                                                                            count+=1
                                                                            tab3.update()
                                                                        elif(running==2):
                                                                            table_1.insert('', index='end',values=("ReadProperty_Multiple%d"%(count),"failed"))
                                                                            continue
                                                                            count+=1
                                                                        else:
                                                                            table_1.insert('', index='end',values=("aborted")) 
                                                                            break
                                                                else:
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break 
                        else:
                            break
                else:
                    break
        else:
            break

def bacnet_write(ip_address,port_no,timedl,obj):
    
    bvlen=random.randrange(24,5238)
    max_apdu=random.randrange(0,80)
    invoke_id=random.randrange(0,256)
    objid1=random.randrange(0,4000,64)
    
    objectinst=random.randrange(0,65536)
    propid1=random.randrange(0,256)
    data1=random.randrange(0,65536)
    data2=random.randrange(0,65536)
    count=1
    
    writep=bacnetwrite(bvlen,max_apdu,invoke_id,objid1,objectinst,propid1,data1,data2)
  
    for bvlen in range(24,65536):  
        if running==0:
            for max_apdu in range(0,256):
                if running==0:
                    for invoke_id in range(0,256):
                        if running==0:
                            for m in range(len(obj)):
                                if running==0:
                                    for objinst in range(0,256):
                                        if running==0:
                                            for propid in range(0,256):
                                                if running==0:
                                                    for data1 in range(0,65536):
                                                        if running==0:
                                                            for data2 in range(0,65536):
                                                                if (((writep[0]==129) and (writep[1]==10) and (writep[4]==1) and (writep[5]==4) and (writep[6]==0) and (writep[9]==15) and (writep[10]==12) and (writep[15]==25) and (writep[17]==62) and (writep[18]==68) and (writep[23]==63)) and running==0):
                                                                    s.sendto(bacnetwrite(bvlen,max_apdu,invoke_id,obj[m],objinst,propid1,data1,data2),(ip_address,port_no))
                                                                   
                                                                    table_1.insert('', index='end',values=("WriteProperty %d"%(count),"passed"))
                                                                    count+=1
                                                                    tab3.after(timedl)
                                                                    tab3.update()
                                                                elif(running==2):    
                                                                    table_1.insert('', index='end',text="WriteProperty %d"%(count),values=("failed"))
                                                                    continue
                                                                    count+=1
                                                                    i+=1
                                                                else:    
                                                                    table_1.insert('', index='end',text="WriteProperty %d"%(count),values=("aborted"))
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
                                                                            
def bacnet_writemultiple(ip_address,port_no,timedl,obj):
    bvlen=random.randrange(16,5238)
    npdu_c=4
    max_apdu=random.randrange(0,80)
    invoke_id=random.randrange(0,256)
    objid1=random.randrange(0,4000,64)
    objinst1=random.randrange(0,65536)
    propid1=random.randrange(0,256)
    d1=random.randrange(0,65536)
    d2=random.randrange(0,256)
    objid2=random.randrange(0,4000,64)
    objinst2=random.randrange(0,256)
    propid2=random.randrange(0,256)
    d3=random.randrange(0,65536)
    d4=random.randrange(0,256)
    count=1
    
    writep=bacnetwritem(bvlen,npdu_c,max_apdu,invoke_id,objid1,objinst1,propid1,d1,d2,objid2,objinst2,propid2,d3,d4)
   
    for bvlen in range(16,65536): 
        if running==0:
            for max_apdu in range(0,256):  
                if running==0:
                    for invoke_id in range(0,256):
                        if running==0:
                            for objid1 in range(0,4000,64): 
                                if running==0:
                                    for objinst1 in range(0,256): 
                                        if running==0:
                                            for propid1 in range(0,256):
                                                if running==0:
                                                    for d1 in range(0,65536):
                                                        if running==0:
                                                            for d2 in range(0,65536):
                                                                if running==0:
                                                                    for m in range(len(obj)): 
                                                                        if running==0:
                                                                            for objinst2 in range(0,256):
                                                                                if running==0:
                                                                                    for propid2 in range(0,256): 
                                                                                        if running==0:
                                                                                            for d3 in range(0,65536):
                                                                                                if running==0:
                                                                                                    for d4  in range(0,65536): 
                                                                                                        if((writep[0]==129) and (writep[1]==10) and (writep[4]==1) and (writep[6]==0) and (writep[6]==0) and (writep[9]==16) and (writep[10]==12) and (writep[15]==30) and (writep[16]==9) and (writep[18]==46) and (writep[19]==68) and (writep[24]==47) and (writep[25]==31) and (writep[26]==12) and (writep[31]==30) and(writep[32]==9) and (writep[34]==46) and (writep[35]==68) and (writep[40]==47) and (writep[41]==31) and running==0):
                                                                                                            s.sendto(bacnetWriteM(bvlen,npdu_c,max_apdu,invoke_id,obj[m],objinst1,propid1,d1,d2,obj[m],objinst2,propid2,d3,d4),(ip_address,port_no))
                                                                                                            table_1.insert('', index='end',values=("Write_Multiple %d"%(count),"passed"))
                                                                                                            count+=1
                                                                                                            tab3.after(timedl)
                                                                                                            tab3.update()
                                                                                                        elif(running==2):
                                                                                                            table_1.insert('', index='end',text="Write_Multiple %d"%(count),values=("failed"))
                                                                                                            continue
                                                                                                            count+=1
                                                                                                            i+=1
                                                                                                        else:
                                                                                                            table_1.insert('', index='end',text="WriteProperty %d"%(count),values=("aborted"))
                                                                                                            break
                                                                                                else:
                                                                                                    break
                                                                                        else:
                                                                                            break
                                                                                else:
                                                                                    break
                                                                        else:
                                                                            break
                                                                else:
                                                                    break
                                                        else:
                                                            break
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
                                     
def bacnet_dcc(ip_address,port_no,timedl):
    
    bvlen=random.randrange(16,65536)
    max_apdu=random.randrange(0,80)
    invoke_id=random.randrange(0,256)
    time_dur=random.randrange(0,256)
    en_dis=random.randrange(0,256)
    passw=random.randrange(0,256)
    count=1
    
    dcc=bacnetdcc(bvlen,max_apdu,invoke_id,time_dur,en_dis,passw)
 
    for bvlen in range(16,65536):
        if running==0:
            for max_apdu in range(0,256):
                if running==0:
                    for invoke_id in range(0,256):
                        if running==0:
                            for time_dur in range(0,256):
                                if running==0:
                                    for en_dis in range(0,256):
                                        if running==0:
                                            for passw in range(0,256):
                                                if ((dcc[0]==129) and (dcc[1]==10) and (dcc[4]==1) and (dcc[5]==4) and (dcc[6]==0) and (dcc[9]==17) and (dcc[10]==9) and (dcc[12]==25) and (dcc[14]==42) and (dcc[15]==0) and running==0):
                                                    s.sendto(bacnetdcc(bvlen,max_apdu,invoke_id,time_dur,en_dis,passw),(ip_address,port_no))
                                                    table_1.insert('', index='end',values=("Device_Communication %d"%(count),"passed"))
                                                    count+=1
                                                    t=tab3.after(timedl)
                                                    tab3.update()
                                                elif(running==2):
                                                    table_1.insert('', index='end',values=("Device_Communication %d"%(count),"failed"))
                                                    continue
                                                    count+=1
                                                else:
                                                    table_1.insert('', index='end',values=("aborted"))
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break

def bacnet_rd(ip_address,port_no,timedl):
    
    bvlen=random.randrange(16,65536)
    max_apdu=random.randrange(0,80)
    invoke_id=random.randrange(0,256)
    device_st=random.randrange(0,256)
    passw=random.randrange(0,256)
    count=1
    
    b_rd=bacnetrd(bvlen,max_apdu,invoke_id,device_st,passw)
    
    for bvlen in range(15,65536):
        if running==0:
            for max_apdu in range(0,256):
                if running==0:
                    for invoke_id in range(0,256):
                        if running==0:
                            for device_st in range(0,256):
                                if running==0:
                                    for passw in range(0,256):
                                        if ((b_rd[0]==129) and (b_rd[1]==10) and(b_rd[4]==1) and (b_rd[5]==4) and (b_rd[6]==0) and (b_rd[9]==20) and (b_rd[10]==9) and (b_rd[12]==26) and (b_rd[13]==0) and running==0):
                                            s.sendto(bacnetrd(bvlen,max_apdu,invoke_id,device_st,passw),(ip_address,port_no))
                                            table_1.insert('', index='end',values=("Reinitialize_Device %d"%(count),"passed"))
                                            count+=1
                                            t=tab3.after(timedl)
                                            tab3.update()
                                        elif(running==2):
                                            table_1.insert('', index='end',values=("Reinitialize_Device %d"%(count),"failed"))
                                            continue
                                            count+=1
                                        else:
                                            table_1.insert('', index='end',values=("aborted"))
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break

def Bacnet_eventinfo(ip_address,port_no,timedl,obj):
    bvlen=random.randrange(15,5238)
    npdu_control=4
    max_apdu=random.randrange(0,256)
    invoke_id=random.randrange(0,256)
    objectid1=random.randrange(0,4000,64)
    objinst=random.randrange(0,256)
    count=1
   
    evinf=bacneteventinformation(bvlen,npdu_control,max_apdu,invoke_id,objectid1,objinst)
    
    for bvlen in range(15,5238):
        if running==0:
            for npdu_cntrl in range(0,80): 
                if running==0:
                    for max_apdusz in range(0,256): 
                        if running==0:
                            for invoke_id in range(0,256):
                                if running==0:
                                    for m in range(len(obj)):
                                        if running==0:
                                            for objinst in range(0,256):
                                                if ((evinf[0]==129) and (evinf[1]==10) and (evinf[4]==1) and (evinf[6]==0) and (evinf[9]==29) and (evinf[10]==12) and running==0):
                                                    s.sendto(bacneteventinformation(bvlen,npdu_control,max_apdu,invoke_id,obj[m],objinst),(ip_address,port_no))                         
                                                    table_1.insert('', index='end',values=("Event Information %d"%(count),"passed"))
                                                    count+=1
                                                    tab3.after(timedl)
                                                    tab3.update()
                                                elif(running==2):
                                                    table_1.insert('', index='end',values=("Alarm Summary %d"%(count),"failed"))
                                                    continue
                                                    count+=1
                                                else:
                                                    table_1.insert('', index='end',values=("aborted"))
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
    

                           

validt_l=ttk.Label(tab3, text="Valid Test Instrumentation")
validt_l.place(x=300,y=25)

col=('1','2')
table_1=ttk.Treeview(tab3,selectmode='browse',column=('1','2'),show='headings',height=20)
table_1.heading('1',text='Packet Number')
table_1.heading('2',text='Packets Sent')
table_1.place(x=300,y=50)

scrollbar = ttk.Scrollbar(tab3,orient="vertical", command=table_1.yview)
table_1.configure(yscroll=scrollbar.set)
scrollbar.place(x=685, y=51, height=425)


def service_choice():
    count=1
    i=1
    size=list2.size()
    sz=list4.size()
    #print('se=',list3.curselection())
    obj1=[]
    for n in range(sz):
            if list4.get(n) in l_obj1:
                obj1.append(l_obj1[list4.get(n)]*64)
    for k in range(size):
        if list3.get(k)=="Acknowledge Alarm":
            bacnet_ack(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="I AM":
            bacnet_iam(target_ip.cget("text"),int(port_number.get()),timed.get())
        if list3.get(k)=="Unconfirmed_Cov":
           bacnet_unconfcov(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Unconfirmed_Event":
            bacnet_unconfevent(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Unconfirmed_Private":
            bacnet_unconfpt(target_ip.cget("text"),int(port_number.get()))
        if list3.get(k)=="Time Syncronization":
            bacnet_timesyn(target_ip.cget("text"),int(port_number.get()),timed.get())
        if list3.get(k)=="UTC Time Syncronization":
            bacnet_utctimesyn(target_ip.cget("text"),int(port_number.get()),timed.get())
        if list3.get(k)=="Who-Is":
            bacnet_whois(target_ip.cget("text"),int(port_number.get()),timed.get())
        if list3.get(k)=="Who-Has":
            bacnet_whohas(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Confirmed_Cov":
            bacnet_concov(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Confirmed_Event":
            bacnet_confevent(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Confirmed_Private":
            bacnet_confpt(target_ip.cget("text"),int(port_number.get()))
        if list3.get(k)=="Alarm Summary":
            bacnet_alarm(target_ip.cget("text"),int(port_number.get()),timed.get())
        if list3.get(k)=="Enrollment Summary":
            bacnet_enroll(target_ip.cget("text"),int(port_number.get()),timed.get())
        if list3.get(k)=="COV":
            bacnet_cov(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Read File":
            bacnet_readfile(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Write File":
            bacnet_writefile(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Add List":
            bacnet_addlist(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Remove List":
            bacnet_removelist(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Create Object":
            bacnet_create(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Delete Object":
            bacnet_delete(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Read Range":
            bacnet_readrange(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Read Property":
           bacnet_read(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Read Multiple":
           bacnet_readmultiple(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Write Property":
            bacnet_write(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Write Multiple":
            bacnet_writemultiple(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
        if list3.get(k)=="Device Communication":
            bacnet_dcc(target_ip.cget("text"),int(port_number.get()),timed.get())
        if list3.get(k)=="Reinitialize Device":
            #table_1.insert('', index='end',text="Testcase 1",values=("In Progress",))
            bacnet_rd(target_ip.cget("text"),int(port_number.get()),timed.get())
        if list3.get(k)=="Event Information":
            #table_1.insert('', index='end',text="Testcase 1",values=("In Progress",))
            bacnet_eventinfo(target_ip.cget("text"),int(port_number.get()),timed.get(),obj1)
           
start = Button(tab3, text="Start",command=service_choice,height=2,width=10)
start.place(x=80, y=130)

def startbtn(event):
    global running
    running=0

start.bind("<Button-1>", startbtn)

def stopbtn():
    start.configure(relief=RAISED)
    global running
    running=1

    
stop= Button(tab3, text= "Stop",command=stopbtn,height=2,width=10)
stop.place(x=80, y=180)

def Close():
    if running==1:
        ws.destroy()
    else:
        messagebox.showerror(title='ERROR',message='Press the Stop Button')
  
  
# Button for closing
exit_button = Button(tab3, text="Exit", command=Close,height=2,width=10)
exit_button.place(x=80,y=280)
    


ws.mainloop()

s.close()
