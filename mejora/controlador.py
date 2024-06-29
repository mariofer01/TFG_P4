from p4utils.utils.helper import load_topo
from p4utils.utils.sswitch_p4runtime_API import SimpleSwitchP4RuntimeAPI
from p4utils.utils.sswitch_thrift_API import SimpleSwitchThriftAPI

topo = load_topo('topology.json')
controllers = {}

for switch, data in topo.get_p4rtswitches().items():
    controllers[switch] = SimpleSwitchP4RuntimeAPI(data['device_id'], data['grpc_port'],
                                                   p4rt_path='mejora_p4rt.txt',
                                                   json_path='mejora.json')

# Configure s1
controller = controllers['s1']

controller.table_add('check_is_ingress_border', 'set_is_ingress_border', ['1'])

controller.table_add('fec_to_label', 'add_mpls_header', ['10.5.2.2/32'], ['200'])
controller.table_add('fec_to_label', 'add_mpls_header', ['10.6.3.2/32'], ['300'])
controller.table_add('fec_to_label', 'add_mpls_header', ['10.10.4.2/32'], ['400'])

controller.table_add('mpls_tbl', 'mpls_forward', ['200'], ['00:00:00:02:01:00', '2'])
controller.table_add('mpls_tbl', 'mpls_forward', ['300'], ['00:00:00:04:01:00', '4'])
controller.table_add('mpls_tbl', 'mpls_forward', ['400'], ['00:00:00:03:01:00', '3'])

controller.table_add('mpls_tbl', 'mpls_forward', ['100'], ['00:00:0a:01:01:02', '1'])

controller.table_add('check_is_egress_border', 'is_egress_border', ['1'])

controller.table_add('ipv4_any', 'ipv4_forward', ['10.5.2.2/32'], ['00:00:00:02:01:00', '2'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.6.3.2/32'], ['00:00:00:04:01:00', '4'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:00:03:01:00', '3'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:0a:01:01:02', '1'])

controller.table_add('ipv4_ef', 'ipv4_forward', ['10.5.2.2/32'], ['00:00:00:03:01:00', '3'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.6.3.2/32'], ['00:00:00:03:01:00', '3'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:00:03:01:00', '3'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:0a:01:01:02', '1'])

# Configure s2
controller = controllers['s2']

controller.table_add('mpls_tbl', 'mpls_forward', ['200'], ['00:00:00:05:02:00', '2'])

controller.table_add('ipv4_any', 'ipv4_forward', ['10.5.2.2/32'], ['00:00:00:05:02:00', '2'])

controller.table_add('ipv4_ef', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:00:01:02:00', '1'])

# Configure s3
controller = controllers['s3']

controller.table_add('mpls_tbl', 'mpls_forward', ['100'], ['00:00:00:01:03:00', '1'])
controller.table_add('mpls_tbl', 'mpls_forward', ['300'], ['00:00:00:06:03:00', '3'])
controller.table_add('mpls_tbl', 'mpls_forward', ['400'], ['00:00:00:05:03:00', '2'])

controller.table_add('ipv4_any', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:00:01:03:00', '1'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.6.3.2/32'], ['00:00:00:06:03:00', '3'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:00:05:03:00', '2'])

controller.table_add('ipv4_ef', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:00:01:03:00', '1'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.5.2.2/32'], ['00:00:00:05:03:00', '2'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.6.3.2/32'], ['00:00:00:06:03:00', '3'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:00:06:03:00', '3'])

# Configure s4
controller = controllers['s4']

controller.table_add('mpls_tbl', 'mpls_forward', ['300'], ['00:00:00:06:04:00', '2'])

controller.table_add('ipv4_any', 'ipv4_forward', ['10.6.3.2/32'], ['00:00:00:06:04:00', '2'])

controller.table_add('ipv4_ef', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:00:01:04:00', '1'])

# Configure s5
controller = controllers['s5']

controller.table_add('check_is_ingress_border', 'set_is_ingress_border', ['1'])

controller.table_add('fec_to_label', 'add_mpls_header', ['10.1.1.2/32'], ['100'])
controller.table_add('fec_to_label', 'add_mpls_header', ['10.6.3.2/32'], ['300'])
controller.table_add('fec_to_label', 'add_mpls_header', ['10.10.4.2/32'], ['400'])

controller.table_add('mpls_tbl', 'mpls_forward', ['100'], ['00:00:00:03:05:00', '3'])
controller.table_add('mpls_tbl', 'mpls_forward', ['300'], ['00:00:00:03:05:00', '3'])
controller.table_add('mpls_tbl', 'mpls_forward', ['400'], ['00:00:00:08:05:00', '4'])

controller.table_add('mpls_tbl', 'mpls_forward', ['200'], ['00:00:0a:05:02:02', '1'])

controller.table_add('check_is_egress_border', 'is_egress_border', ['1'])

controller.table_add('ipv4_any', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:00:03:05:00', '3'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.6.3.2/32'], ['00:00:00:03:05:00', '3'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:00:08:05:00', '4'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.5.2.2/32'], ['00:00:0a:05:02:02', '1'])

controller.table_add('ipv4_ef', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:00:02:05:00', '2'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.6.3.2/32'], ['00:00:00:08:05:00', '4'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:00:07:05:00', '5'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.5.2.2/32'], ['00:00:0a:05:02:02', '1'])

# Configure s6
controller = controllers['s6']

controller.table_add('check_is_ingress_border', 'set_is_ingress_border', ['1'])

controller.table_add('fec_to_label', 'add_mpls_header', ['10.1.1.2/32'], ['100'])
controller.table_add('fec_to_label', 'add_mpls_header', ['10.5.2.2/32'], ['200'])
controller.table_add('fec_to_label', 'add_mpls_header', ['10.10.4.2/32'], ['400'])

controller.table_add('mpls_tbl', 'mpls_forward', ['100'], ['00:00:00:03:06:00', '3'])
controller.table_add('mpls_tbl', 'mpls_forward', ['200'], ['00:00:00:08:06:00', '4'])
controller.table_add('mpls_tbl', 'mpls_forward', ['400'], ['00:00:00:08:06:00', '4'])

controller.table_add('mpls_tbl', 'mpls_forward', ['300'], ['00:00:0a:06:03:02', '1'])

controller.table_add('check_is_egress_border', 'is_egress_border', ['1'])

controller.table_add('ipv4_any', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:00:03:06:00', '3'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.5.2.2/32'], ['00:00:00:08:06:00', '4'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:00:08:06:00', '4'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.6.3.2/32'], ['00:00:0a:06:03:02', '1'])

controller.table_add('ipv4_ef', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:00:04:06:00', '2'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.5.2.2/32'], ['00:00:00:03:06:00', '3'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:00:09:06:00', '5'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.6.3.2/32'], ['00:00:0a:06:03:02', '1'])

# Configure s7
controller = controllers['s7']

controller.table_add('mpls_tbl', 'mpls_forward', ['200'], ['00:00:00:05:07:00', '2'])

controller.table_add('ipv4_any', 'ipv4_forward', ['10.5.2.2/32'], ['00:00:00:05:07:00', '2'])

controller.table_add('ipv4_ef', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:00:0a:07:00', '1'])

# Configure s8
controller = controllers['s8']

controller.table_add('mpls_tbl', 'mpls_forward', ['100'], ['00:00:00:06:08:00', '3'])
controller.table_add('mpls_tbl', 'mpls_forward', ['200'], ['00:00:00:05:08:00', '2'])
controller.table_add('mpls_tbl', 'mpls_forward', ['400'], ['00:00:00:0a:08:00', '1'])

controller.table_add('ipv4_any', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:00:06:08:00', '3'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.5.2.2/32'], ['00:00:00:05:08:00', '2'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:00:0a:08:00', '1'])

controller.table_add('ipv4_ef', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:00:05:08:00', '2'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.5.2.2/32'], ['00:00:00:05:08:00', '2'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.6.3.2/32'], ['00:00:00:06:08:00', '3'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:00:0a:08:00', '1'])

# Configure s9
controller = controllers['s9']

controller.table_add('mpls_tbl', 'mpls_forward', ['300'], ['00:00:00:06:09:00', '2'])

controller.table_add('ipv4_any', 'ipv4_forward', ['10.6.3.2/32'], ['00:00:00:06:09:00', '2'])

controller.table_add('ipv4_ef', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:00:0a:09:00', '1'])

# Configure s10
controller = controllers['s10']

controller.table_add('check_is_ingress_border', 'set_is_ingress_border', ['1'])

controller.table_add('fec_to_label', 'add_mpls_header', ['10.1.1.2/32'], ['100'])
controller.table_add('fec_to_label', 'add_mpls_header', ['10.5.2.2/32'], ['200'])
controller.table_add('fec_to_label', 'add_mpls_header', ['10.6.3.2/32'], ['300'])

controller.table_add('mpls_tbl', 'mpls_forward', ['100'], ['00:00:00:08:0a:00', '3'])
controller.table_add('mpls_tbl', 'mpls_forward', ['200'], ['00:00:00:07:0a:00', '2'])
controller.table_add('mpls_tbl', 'mpls_forward', ['300'], ['00:00:00:09:0a:00', '4'])

controller.table_add('mpls_tbl', 'mpls_forward', ['400'], ['00:00:0a:0a:04:02', '1'])

controller.table_add('check_is_egress_border', 'is_egress_border', ['1'])

controller.table_add('ipv4_any', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:00:08:0a:00', '3'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.5.2.2/32'], ['00:00:00:07:0a:00', '2'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.6.3.2/32'], ['00:00:00:09:0a:00', '4'])
controller.table_add('ipv4_any', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:0a:0a:04:02', '1'])

controller.table_add('ipv4_ef', 'ipv4_forward', ['10.1.1.2/32'], ['00:00:00:08:0a:00', '3'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.5.2.2/32'], ['00:00:00:08:0a:00', '3'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.6.3.2/32'], ['00:00:00:08:0a:00', '3'])
controller.table_add('ipv4_ef', 'ipv4_forward', ['10.10.4.2/32'], ['00:00:0a:0a:04:02', '1'])
