import classes from './RequestList.module.scss'
import RequestCard from './Request/RequestCard'
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from 'axios';
import PanelCard from '../RequestPanel/PanelCard/PanelCard';


const RequestList = (props: {status: string}) => {
    const [requests, setRequests] = useState<Array<{
        id: Int16Array,
        student: {
          surname: string,
          name: string,
          patronymic: string,
          username: string,
          role: string
        };
        lab: {
          id: Int16Array,
          name: string,
          description: string,
          semester: number,
          qroupname: string,
          deadline: Date
        };
        content: string;
        comments: string;
        variant: Int16Array;
        info: {};
        lecturer: {
          surname: string,
          name: string,
          patronymic: string,
          username: string,
          role: string
        };
        status: string;
        creationdate: Date;
    }>>([]);
    const navigate = useNavigate();

    const [selectedStatus, setSelectedStatus] = useState("Pending");

    const handleStatusChange = (newStatus: string) => {
      setSelectedStatus(newStatus);
    };

    useEffect(() => {
        const fetchRequests = async () => {
          const { data } = await axios.get(
            "http://127.0.0.1:8000/api/cards?sessionKey=123"
          );
          const requests = Object.values(data) as any[];
          console.log(requests)

          setRequests(requests.map((request) => ({
            id: request.id,
            student: {
              surname: request.student.surname,
              name: request.student.name,
              patronymic: request.student.patronymic,
              username: request.student.username,
              role: request.student.role
            },
            lab: {
              id: request.lab.id,
              name: request.lab.name,
              description: request.lab.description,
              semester: request.lab.semester,
              qroupname: request.lab.groupname,
              deadline: request.lab.deadline
            },
            content: request.content,
            comments: request.comments,
            variant: request.variant,
            info: request.info,
            lecturer: {
              surname: request.lecturer.surname,
              name: request.lecturer.name,
              patronymic: request.lecturer.patronymic,
              username: request.lecturer.username,
              role: request.lecturer.role
            },
            status: request.status,
            creationdate: request.creationdate
          })));
        };

        fetchRequests();
      }, []);
    return( <>
    <div className = {classes.container}>
        <div className={classes.wrap}>
            {requests.filter((request) => request.status === selectedStatus).map((item) => 
                <RequestCard
                    name={`${item.student.surname} ${item.student.name} ${item.student.patronymic}`}
                    number={item.lab.qroupname}
                    work={item.lab.name}
                    semester={item.lab.semester}
                    date={item.creationdate}
                    deadline={item.lab.deadline}
                    onClick={() => navigate("/LabInfo", {state: item})}
                />
            )}
        </div>
        </div>
    </>
    );
}

export default RequestList;