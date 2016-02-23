<scriptConfig name="VRT2" script="VRT">
  <params>
    <param name="vrt.settings.time_window" type="int">0</param>
    <param name="vrt.settings.ramp_time" type="int">0</param>
    <param name="vrt.settings.timeout_period" type="int">0</param>
    <param name="invt.time_msa" type="float">0.1</param>
    <param name="vrt.settings.l_curve_num" type="int">1</param>
    <param name="invt.test_point_offset" type="float">1.0</param>
    <param name="vrt.settings.h_curve_num" type="int">1</param>
    <param name="vrt.settings.h_n_points" type="int">3</param>
    <param name="vrt.settings.l_n_points" type="int">5</param>
    <param name="invt.VRT_period" type="int">5</param>
    <param name="invt.verification_delay" type="int">5</param>
    <param name="invt.posttest_delay" type="int">10</param>
    <param name="invt.pretest_delay" type="int">10</param>
    <param name="invt.failure_count" type="int">60</param>
    <param name="comm.slave_id" type="int">126</param>
    <param name="comm.ipport" type="int">502</param>
    <param index_count="3" index_start="1" name="vrt.h_curve.h_time" type="float">0.16 13.0 13.0 </param>
    <param index_count="3" index_start="1" name="vrt.h_curve.h_volt" type="float">120.0 120.0 110.0 </param>
    <param index_count="5" index_start="1" name="vrt.l_curve.l_time" type="float">0.16 11.0 11.0 21.0 21.0 </param>
    <param index_count="5" index_start="1" name="vrt.l_curve.l_volt" type="float">45.0 45.0 60.0 60.0 88.0 </param>
    <param name="wfm.pretrig" type="string">1</param>
    <param name="wfm.trighyswindow" type="string">10.000e-3</param>
    <param name="comm.ipaddr" type="string">192.168.0.173</param>
    <param name="wfm.trigsamplingrate" type="string">24.0e3</param>
    <param name="wfm.trigval" type="string">3.000</param>
    <param name="wfm.trigtimeout" type="string">30</param>
    <param name="wfm.posttrig" type="string">5.000</param>
    <param name="wfm.trigchannel" type="string">AC_Voltage_10</param>
    <param name="wfm.trigacqchannels" type="string">AC_Voltage_10, AC_Current_10, Ametek_Trigger</param>
    <param name="gridsim.auto_config" type="string">Disabled</param>
    <param name="wfm.trigcondition" type="string">Falling Edge</param>
    <param name="pvsim.mode" type="string">Manual</param>
    <param name="gridsim.mode" type="string">Manual</param>
    <param name="invt.disable" type="string">No</param>
    <param name="vrt.settings.ride_through" type="string">No</param>
    <param name="datatrig.dsm_method" type="string">Sandia LabView DSM</param>
    <param name="comm.ifc_type" type="string">TCP</param>
  </params>
</scriptConfig>
