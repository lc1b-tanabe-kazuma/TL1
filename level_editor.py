import bpy

# ブレンダーに登録するアドオン情報
bl_info = {
    "name":"レベルエディタ",
    "author":"Tanabe",
    "version":(1,0),
    "blender":(3,6,1),
    "location":"",
    "description":"レベルエディタ",
    "warning":"",
    "wiki_url":"",
    "tracker_url":"",
    "category":"Object"
}

#アドオン有効時のコールバック
def register():
    print("レベルエディタが有効化されました")

def unregister():
    print("レベルエディタが無効化されました")
    
if __name__ == "__main__":
    register()