CREATE TABLE FILESTATE
(
    ID              VARCHAR(255)        NOT NULL,
    Filepath        VARCHAR(255)        NOT NULL,
    Hashval         VARCHAR(64)         NOT NULL,
    Timecode        TIMESTAMP           DEFAULT CURRENT_TIMESTAMP
);