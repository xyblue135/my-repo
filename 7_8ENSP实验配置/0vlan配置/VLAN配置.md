简而言之，Access端口不需要PVID，因为它只服务于一个VLAN，所有流量都默认属于该VLAN。而Trunk端口需要PVID来处理未标记的帧，确保它们能够被正确地归类到一个VLAN中去。
### Access端口
Access端口用于连接终端设备，如计算机、电话或打印机。这些端口通常只属于一个VLAN，所有进出Access端口的流量都会被自动标记为此端口所属的VLAN。因为Access端口只服务于一个VLAN，所以它不需要PVID。当你在Access端口上发送或接收数据时，数据帧不会携带VLAN标签，因为Access端口默认将所有未标记的帧视为属于该端口的VLAN。
### Trunk端口
Trunk端口则不同，它们用于连接两个交换机或其他网络设备，可以承载多个VLAN的流量。Trunk端口需要处理来自多个VLAN的流量，并且能够区分和转发这些不同VLAN的流量。为了做到这一点，所有通过Trunk端口的数据帧都会携带VLAN标签。
然而，Trunk端口也需要处理一种特殊情况，那就是未标记的帧。未标记的帧可能来自于某个配置错误的设备，或者是在某些场景下故意发送的。在这种情况下，Trunk端口需要知道如何处理这些未标记的帧，这就需要用到PVID。
PVID指定了Trunk端口的默认VLAN，当Trunk端口接收到未标记的帧时，它会自动将此帧标记为PVID所指定的VLAN。因此，PVID对于Trunk端口来说是必要的，它确保了未标记帧能够被正确地分类和转发。
```
sy
vlan batch 10 20
int 接口
port link-type access/trunk?
port trunk allow-pass vlan all
port default default vlan 10
```

```
port trunk pvid vlan 10
```

# TRUNK模式
1. 进入接口配置模式：首先，我们需要选择要进行配置的接口，并进入其配置模式。在eNSP中，可以通过命令行界面（CLI）或者图形用户界面（GUI）来进行操作。
2. 设置Native VLAN：Native VLAN是指在Trunk模式下，接口默认所属的VLAN。在eNSP中，可以通过命令`port trunk pvid vlan [vlan-id]`来设置Native VLAN。例如，要将接口的Native VLAN设置为VLAN 1，可以执行命令`port trunk pvid vlan 1`。
3. 允许通过的VLAN列表：在Trunk模式下，我们需要指定哪些VLAN的数据可以通过该接口传输。这可以通过命令`port trunk allow-pass vlan [vlan-id-list]`来实现。例如，要允许VLAN 10和VLAN 20的数据通过接口传输，可以执行命令`port trunk allow-pass vlan 10 20`。