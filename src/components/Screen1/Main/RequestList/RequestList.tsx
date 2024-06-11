import classes from './RequestList.module.scss'
import RequestCard from './Request/RequestCard'
import { useNavigate } from "react-router-dom";
import { useEffect, useState} from "react";
import axios from 'axios';

const RequestList = (props: {status: string, sesKey: string}) => {
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
        content: URL;
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

    console.log(`http://127.0.0.1:8000/api/card?sessionKey=${props.sesKey}`)

    useEffect(() => {
        const fetchRequests = async () => {
          const { data } = await axios.get(
            `http://127.0.0.1:8000/api/card?sessionKey=${props.sesKey}`
          );
          const requests = Object.values(data) as any[];
          console.log(requests)
          console.log(props.sesKey)

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
            {requests.filter((request) => request.status === props.status).map((item) => 
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