#ifndef __BTSTACK_H
#define __BTSTACK_H

#include "btstack_config.h"

#include "bluetooth.h"
#include "bluetooth_data_types.h"
#include "bluetooth_gatt.h"
#include "bluetooth_sdp.h"
#include "bluetooth_company_id.h"
#include "ad_parser.h"
#include "btstack_control.h"
#include "btstack_debug.h"
#include "btstack_event.h"
#include "btstack_defines.h"
#include "btstack_linked_list.h"
#include "btstack_memory.h"
#include "btstack_memory_pool.h"
#include "btstack_run_loop.h"
#include "btstack_util.h"
#include "gap.h"
#include "hci.h"
#include "hci_cmd.h"
#include "hci_dump.h"
#include "hci_transport.h"
#include "l2cap.h"
#include "l2cap_signaling.h"

#ifdef ENABLE_BLE
#include "ble/ancs_client.h"
#include "ble/att_db.h"
#include "ble/att_db_util.h"
#include "ble/att_dispatch.h"
#include "ble/att_server.h"
#include "ble/gatt_client.h"
#include "ble/le_device_db.h"
#include "ble/sm.h"
#endif

// #ifdef ENABLE_CLASSIC
#include "classic/bnep.h"
#include "classic/btstack_link_key_db.h"
#include "classic/device_id_server.h"
#include "classic/hfp.h"
#include "classic/hfp_ag.h"
#include "classic/hfp_hf.h"
#include "classic/hid_device.h"
#include "classic/hsp_ag.h"
#include "classic/hsp_hs.h"
#include "classic/pan.h"
#include "classic/rfcomm.h"
#include "classic/sdp_client.h"
#include "classic/sdp_client_rfcomm.h"
#include "classic/sdp_server.h"
#include "classic/sdp_util.h"
#include "classic/spp_server.h"
// #endif

#endif  // __BTSTACK_H
 