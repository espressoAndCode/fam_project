CREATE TABLE FILESTATE
(
    ID              VARCHAR(255)        NOT NULL,
    Filepath        VARCHAR(255)        NOT NULL,
    Hashval         VARCHAR(64)         NOT NULL,
    Timecode        TIMESTAMP           DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE EVENTLOG
(
    Timecode        DATETIME            NOT NULL,
    Filepath        VARCHAR(255)        NOT NULL,
    Syscall         VARCHAR(64)         NOT NULL,
    Success         INT                 NOT NULL,
    Exe             VARCHAR(255)        NOT NULL,
    Auid            VARCHAR(64)         NOT NULL          
);