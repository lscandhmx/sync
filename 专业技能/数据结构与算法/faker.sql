


select city_name as `城市`
      ,day_key as `日期`
      ,hour_key as `小时`
      ,count(distinct order_no) as `荣耀分排序订单数`
      ,count(distinct if(choose_driver_cnt>1,order_no,null)) as `荣耀分排序司机数>1订单数`
      ,count(distinct if(choose_driver_cnt>1,order_no,null))/count(distinct order_no) as `荣耀分PK发生率`
      ,count(distinct if(key_choose_driver_cnt>0,order_no,null)) as `荣耀分排序核心司机数>0订单数`
      ,count(distinct if(key_choose_driver_cnt>1,order_no,null)) as `荣耀分排序核心司机数>1订单数`
      ,count(distinct if(key_choose_driver_cnt>0,order_no,null))/count(distinct order_no) as `荣耀分核心司机入围率`
      ,count(distinct if(key_choose_driver_cnt>0 and choose_driver_cnt>1,order_no,null)) as `荣耀分PK核心司机入围订单数`
      ,count(distinct if(key_choose_driver_cnt>0 and choose_driver_cnt>1,order_no,null))/count(distinct if(choose_driver_cnt>1,order_no,null)) as `荣耀分PK核心司机入围率`
      ,count(distinct if(rece_driver_cnt>0,order_no,null)) as `实时单接单数`
      ,count(distinct if(rece_driver_cnt>0 and is_top1_driver_score>0,order_no,null)) as `接单司机为荣耀分排序TOP1订单数`
      ,count(distinct if(rece_driver_cnt>0 and is_top1_driver_score>0,order_no,null))/count(distinct if(rece_driver_cnt>0,order_no,null)) as `荣耀分TOP1司机接单率`
      ,count(distinct if(rece_driver_cnt>0 and is_top1_driver_score>0 and choose_driver_cnt>1,order_no,null)) as `荣耀分PK TOP1司机接单数`
      ,count(distinct if(rece_driver_cnt>0 and choose_driver_cnt>1,order_no,null)) as `荣耀分PK接单数`
      ,count(distinct if(rece_driver_cnt>0 and is_top1_driver_score>0 and choose_driver_cnt>1,order_no,null))/count(if(rece_driver_cnt>0 and choose_driver_cnt>1,order_no,null)) as `荣耀分PK TOP1司机接单率`
      ,count(distinct if(rece_driver_cnt>0 and is_top1_level_driver_score>0 and choose_driver_cnt>1,order_no,null)) as `荣耀分PK TOP1档司机接单数`
      ,count(distinct if(rece_driver_cnt>0 and is_top1_level_driver_score>0 and choose_driver_cnt>1,order_no,null))/count(if(rece_driver_cnt>0 and choose_driver_cnt>1,order_no,null)) as `荣耀分PK TOP1档司机接单率`
from
(
    select city_name
          ,day_key
          ,hour_key
          ,a.order_no
          ,distance_ro
          ,distance_level
          ,nvl(rece_distance_ro,10) as rece_distance_ro
          ,count(distinct sort_driverNo) as choose_driver_cnt
          ,count(distinct if(is_core_driver=1,sort_driverNo,null)) as key_choose_driver_cnt
          ,count(distinct if(is_rece=1 and is_rece_driver=1,rece_driver_no,null)) as rece_driver_cnt
          ,count(distinct if(is_rece=1 and is_core_driver=1 and is_rece_driver=1,rece_driver_no,null)) as key_rece_driver_cnt
          ,if(sum(is_rece_driver)=1 and avg(rece_driver_score)>=max(sort_driver_score),1,0) as is_top1_driver_score
          ,if(sum(is_rece_driver)=1 and sum(if(is_rece_driver=1,servicepoint,0))>=max(servicepoint),1,0) as is_top1_level_driver_score
    from
    order_sort_detail a
    left join
    (select order_no,distance_ro as rece_distance_ro from order_sort_detail where is_rece_driver=1) b
    on a.order_no=b.order_no
    group by 1,2,3,4,5,6,7
)
where distance_ro is not null and distance_ro<=rece_distance_ro
group by 1,2,3

class Solution:
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
            if !pHead1:
