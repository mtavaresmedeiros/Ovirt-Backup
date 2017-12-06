##### Verificando se a vm ja possui snapshot

class vmtools:
    def check_snap(self,vm_service):
        snaps_service = vm_service.snapshots_service()
        snaps = snaps_service.list()
        snap_check = next((s for s in snaps if s.description == snap_description),None)


##### Apagando snapshot
    def delete_snapshot(self,vm_service):
        if snap_check :
            snap_service = snaps_service.snapshot_service(snap_check.id)
            snap_service.remove()
            count = 0
            while True :
                if snap_check :
                    snap_service = snaps_service.snapshot_service(snap_check.id)
                    snaps = snaps_service.list()
                    if next((s for s in snaps if s.description == snap_description),None) :
                        snap = snap_service.get()
                        if snap.snapshot_status == types.SnapshotStatus.OK and count != 2:
                            snaps_service = vm_service.snapshots_service()
                            snap_service.remove()
                            count += 1
                    time.sleep(1)
                    count += 1
                else:
                    break
                snaps_service = vm_service.snapshots_service()
                snaps = snaps_service.list()
                snap_check = next((s for s in snaps if s.description == snap_description),None)
    except Exception as e:
        continue

"""""        
    ##### criando snapshot
    snaps_service = vm_service.snapshots_service()
    snap = snaps_service.add(
                           snapshot=types.Snapshot(
                           description=snap_description,
                           persist_memorystate=False,
                           ),
                           )

    ##### Verificando Estado do Snapshot

    snap_service = snaps_service.snapshot_service(snap.id)

    while snap.snapshot_status != types.SnapshotStatus.OK:
        time.sleep(1)
        snap = snap_service.get()

"""""

