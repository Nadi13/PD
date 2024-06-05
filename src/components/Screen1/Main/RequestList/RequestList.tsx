import classes from './RequestList.module.scss'
import RequestCard from './Request/RequestCard'
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from 'axios';


const RequestList = () => {
    const [requests, setRequests] = useState<Array<{
        name: string;
        number: string;
        work: string;
        course: string;
        date: string;
        deadline: boolean;
    }>>([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchRequests = async () => {
          const { data } = await axios.get(
            "http://127.0.0.1:8000/api/user?sessionKey=123"
          );
          const requests = Object.values(data) as any[];
          console.log(requests)

          setRequests(requests.map((request) => ({
            name: request.name,
            number: request.number,
            work: request.work,
            course: request.course,
            date: request.date,
            deadline: request.deadline
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