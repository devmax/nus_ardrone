"""autogenerated by genpy from AutoNav/obs_tag.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class obs_tag(genpy.Message):
  _md5sum = "7243c87b8f2184b88b97eb8563a878d4"
  _type = "AutoNav/obs_tag"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 timestamp
uint32 seq

int32 rejected

float32 roll_raw
float32 pitch_raw
float32 yaw_raw

# the observation
float32 x
float32 y
float32 z
float32 roll
float32 pitch
float32 yaw

#the prior
float32 x_pre
float32 y_pre
float32 z_pre
float32 dx_pre
float32 dy_pre
float32 dz_pre
float32 roll_pre
float32 pitch_pre
float32 yaw_pre
float32 dyaw_pre

#the posterior
float32 x_post
float32 y_post
float32 z_post
float32 dx_post
float32 dy_post
float32 dz_post
float32 roll_post
float32 pitch_post
float32 yaw_post
float32 dyaw_post
"""
  __slots__ = ['timestamp','seq','rejected','roll_raw','pitch_raw','yaw_raw','x','y','z','roll','pitch','yaw','x_pre','y_pre','z_pre','dx_pre','dy_pre','dz_pre','roll_pre','pitch_pre','yaw_pre','dyaw_pre','x_post','y_post','z_post','dx_post','dy_post','dz_post','roll_post','pitch_post','yaw_post','dyaw_post']
  _slot_types = ['int32','uint32','int32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timestamp,seq,rejected,roll_raw,pitch_raw,yaw_raw,x,y,z,roll,pitch,yaw,x_pre,y_pre,z_pre,dx_pre,dy_pre,dz_pre,roll_pre,pitch_pre,yaw_pre,dyaw_pre,x_post,y_post,z_post,dx_post,dy_post,dz_post,roll_post,pitch_post,yaw_post,dyaw_post

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(obs_tag, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timestamp is None:
        self.timestamp = 0
      if self.seq is None:
        self.seq = 0
      if self.rejected is None:
        self.rejected = 0
      if self.roll_raw is None:
        self.roll_raw = 0.
      if self.pitch_raw is None:
        self.pitch_raw = 0.
      if self.yaw_raw is None:
        self.yaw_raw = 0.
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.z is None:
        self.z = 0.
      if self.roll is None:
        self.roll = 0.
      if self.pitch is None:
        self.pitch = 0.
      if self.yaw is None:
        self.yaw = 0.
      if self.x_pre is None:
        self.x_pre = 0.
      if self.y_pre is None:
        self.y_pre = 0.
      if self.z_pre is None:
        self.z_pre = 0.
      if self.dx_pre is None:
        self.dx_pre = 0.
      if self.dy_pre is None:
        self.dy_pre = 0.
      if self.dz_pre is None:
        self.dz_pre = 0.
      if self.roll_pre is None:
        self.roll_pre = 0.
      if self.pitch_pre is None:
        self.pitch_pre = 0.
      if self.yaw_pre is None:
        self.yaw_pre = 0.
      if self.dyaw_pre is None:
        self.dyaw_pre = 0.
      if self.x_post is None:
        self.x_post = 0.
      if self.y_post is None:
        self.y_post = 0.
      if self.z_post is None:
        self.z_post = 0.
      if self.dx_post is None:
        self.dx_post = 0.
      if self.dy_post is None:
        self.dy_post = 0.
      if self.dz_post is None:
        self.dz_post = 0.
      if self.roll_post is None:
        self.roll_post = 0.
      if self.pitch_post is None:
        self.pitch_post = 0.
      if self.yaw_post is None:
        self.yaw_post = 0.
      if self.dyaw_post is None:
        self.dyaw_post = 0.
    else:
      self.timestamp = 0
      self.seq = 0
      self.rejected = 0
      self.roll_raw = 0.
      self.pitch_raw = 0.
      self.yaw_raw = 0.
      self.x = 0.
      self.y = 0.
      self.z = 0.
      self.roll = 0.
      self.pitch = 0.
      self.yaw = 0.
      self.x_pre = 0.
      self.y_pre = 0.
      self.z_pre = 0.
      self.dx_pre = 0.
      self.dy_pre = 0.
      self.dz_pre = 0.
      self.roll_pre = 0.
      self.pitch_pre = 0.
      self.yaw_pre = 0.
      self.dyaw_pre = 0.
      self.x_post = 0.
      self.y_post = 0.
      self.z_post = 0.
      self.dx_post = 0.
      self.dy_post = 0.
      self.dz_post = 0.
      self.roll_post = 0.
      self.pitch_post = 0.
      self.yaw_post = 0.
      self.dyaw_post = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_iIi29f.pack(_x.timestamp, _x.seq, _x.rejected, _x.roll_raw, _x.pitch_raw, _x.yaw_raw, _x.x, _x.y, _x.z, _x.roll, _x.pitch, _x.yaw, _x.x_pre, _x.y_pre, _x.z_pre, _x.dx_pre, _x.dy_pre, _x.dz_pre, _x.roll_pre, _x.pitch_pre, _x.yaw_pre, _x.dyaw_pre, _x.x_post, _x.y_post, _x.z_post, _x.dx_post, _x.dy_post, _x.dz_post, _x.roll_post, _x.pitch_post, _x.yaw_post, _x.dyaw_post))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 128
      (_x.timestamp, _x.seq, _x.rejected, _x.roll_raw, _x.pitch_raw, _x.yaw_raw, _x.x, _x.y, _x.z, _x.roll, _x.pitch, _x.yaw, _x.x_pre, _x.y_pre, _x.z_pre, _x.dx_pre, _x.dy_pre, _x.dz_pre, _x.roll_pre, _x.pitch_pre, _x.yaw_pre, _x.dyaw_pre, _x.x_post, _x.y_post, _x.z_post, _x.dx_post, _x.dy_post, _x.dz_post, _x.roll_post, _x.pitch_post, _x.yaw_post, _x.dyaw_post,) = _struct_iIi29f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_iIi29f.pack(_x.timestamp, _x.seq, _x.rejected, _x.roll_raw, _x.pitch_raw, _x.yaw_raw, _x.x, _x.y, _x.z, _x.roll, _x.pitch, _x.yaw, _x.x_pre, _x.y_pre, _x.z_pre, _x.dx_pre, _x.dy_pre, _x.dz_pre, _x.roll_pre, _x.pitch_pre, _x.yaw_pre, _x.dyaw_pre, _x.x_post, _x.y_post, _x.z_post, _x.dx_post, _x.dy_post, _x.dz_post, _x.roll_post, _x.pitch_post, _x.yaw_post, _x.dyaw_post))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 128
      (_x.timestamp, _x.seq, _x.rejected, _x.roll_raw, _x.pitch_raw, _x.yaw_raw, _x.x, _x.y, _x.z, _x.roll, _x.pitch, _x.yaw, _x.x_pre, _x.y_pre, _x.z_pre, _x.dx_pre, _x.dy_pre, _x.dz_pre, _x.roll_pre, _x.pitch_pre, _x.yaw_pre, _x.dyaw_pre, _x.x_post, _x.y_post, _x.z_post, _x.dx_post, _x.dy_post, _x.dz_post, _x.roll_post, _x.pitch_post, _x.yaw_post, _x.dyaw_post,) = _struct_iIi29f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_iIi29f = struct.Struct("<iIi29f")