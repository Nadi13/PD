import classes from './RequestList.module.scss'
import RequestCard from './Request/RequestCard'
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from 'axios';


const RequestList = () => {
    const [requests, setRequests] = useState<Array<{
        id: Int16Array,
        studenid: string;
        labid: string;
        content: string;
        comments: string;
        lecturerid: string;
        variant: Int16Array;
        info: {};
        status: string;
        creationdate: Date;
    }>>([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchRequests = async () => {
          const { data } = await axios.get(
            "http://127.0.0.1:8000/api/cards?sessionKey=123"
          );
          const requests = Object.values(data) as any[];
          console.log(requests)

          setRequests(requests.map((request) => ({
            id: request.id,
            studenid: request.studentid,
            labid: request.labid,
            content: request.content,
            comments: request.comments,
            lecturerid: request.lecturerid,
            variant: request.variant,
            info: request.info,
            status: request.status,
            creationdate: request.creationdate
          })));
        };

        fetchRequests();
      }, []);


    return( <>
    <div className = {classes.container}>
        <div className={classes.wrap}>
            {requests.map((item) => 
                <RequestCard
                    name={item.name}
                    number={item.number}
                    work={item.work}
                    course={item.course}
                    date={item.date}
                    deadline={item.deadline}
                    onClick={() => navigate("/LabInfo", {state: item})}
                />
            )}
        </div>
        </div>
    </>
    );
}

export default RequestList;