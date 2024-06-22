from p4utils.utils.sswitch_p4runtime_API import SimpleSwitchP4RuntimeAPI

controller = SimpleSwitchP4RuntimeAPI(device_id=1, grpc_port=9559,
                                      p4rt_path='basico_p4rt.txt',
                                      json_path='basico.json')

#controller.table_clear('ipv4_lpm')
controller.table_set_default('ipv4_lpm','drop')
controller.table_add('ipv4_lpm', 'ipv4_forward',['10.0.1.1/32'], ['00:00:0a:00:01:01','1'])
controller.table_add('ipv4_lpm', 'ipv4_forward',['10.0.2.0/24'], ['00:00:00:02:01:00','2'])
controller.table_add('ipv4_lpm', 'ipv4_forward',['10.0.3.0/24'], ['00:00:00:03:01:00','3'])

controller = SimpleSwitchP4RuntimeAPI(device_id=2, grpc_port=9560,
                                      p4rt_path='basico_p4rt.txt',
                                      json_path='basico.json')

#controller.table_clear('ipv4_lpm')
controller.table_set_default('ipv4_lpm','drop')
controller.table_add('ipv4_lpm', 'ipv4_forward',['10.0.1.0/24'], ['00:00:00:01:02:00','2'])
controller.table_add('ipv4_lpm', 'ipv4_forward',['10.0.2.2/32'], ['00:00:0a:00:02:02','1'])
controller.table_add('ipv4_lpm', 'ipv4_forward',['10.0.3.0/24'], ['00:00:00:01:02:00','2'])

controller = SimpleSwitchP4RuntimeAPI(device_id=3, grpc_port=9561,
                                      p4rt_path='basico_p4rt.txt',
                                      json_path='basico.json')

#controller.table_clear('ipv4_lpm')
controller.table_set_default('ipv4_lpm','drop')
controller.table_add('ipv4_lpm', 'ipv4_forward',['10.0.1.0/24'], ['00:00:00:01:03:00','3'])
controller.table_add('ipv4_lpm', 'ipv4_forward',['10.0.2.0/24'], ['00:00:00:01:03:00','3'])
controller.table_add('ipv4_lpm', 'ipv4_forward',['10.0.3.3/32'], ['00:00:0a:00:03:03','1'])
controller.table_add('ipv4_lpm', 'ipv4_forward',['10.0.3.4/32'], ['00:00:0a:00:03:04','2'])
