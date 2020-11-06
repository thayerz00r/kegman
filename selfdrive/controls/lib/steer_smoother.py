class SteerSmoother():
  def __init__(self):
    self.data_rst = 0
    self.data_steer = [0.0, 0.0]​

# steer_angle_des smoother
  def get_data(self, steer_angle_dest, stAngle_Diff, reduceRate):
    self.data_steer.pop(0)
    self.data_steer.append(steer_angle_dest)
    if abs(self.data_steer[1] - self.data_steer[0]) > stAngle_Diff:
      self.data_rst = steer_angle_dest * reduceRate
      self.data_steer[1] = self.data_rst #self.data_rst 값을 취함에 주의
    else:
      self.data_rst = steer_angle_dest
    return self.data_rst
