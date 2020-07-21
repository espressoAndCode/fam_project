CREATE TABLE FILESTATE
(
    Filepath        VARCHAR(255)        NOT NULL,
    Hashval         VARCHAR(64)         NOT NULL,
    Watchname       VARCHAR(64)         NOT NULL, 
    Timecode        TIMESTAMP           DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE EVENTLOG
(
    Timecode        DATETIME            NOT NULL,
    Filepath        VARCHAR(255)        NOT NULL,
    Syscall         VARCHAR(64)         NOT NULL,
    Success         INT                 NOT NULL,
    Exe             VARCHAR(255)        NOT NULL,
    Auid            VARCHAR(64)         NOT NULL,
    Watchname       VARCHAR(64)         NOT NULL          
);

CREATE TABLE WATCHES
(
    Watchname       VARCHAR(64)         NOT NULL,
    Filepath        VARCHAR(255)        NOT NULL
);


CREATE TABLE AUTHORIZED
(
    Watchname       VARCHAR(64)         NOT NULL,
    Userid          VARCHAR(64)         NOT NULL
);