INSERT INTO FILESTATE VALUES ('testfile.txt', '386bd2c34146659559b2187de1b601b5f8c8208153d7953275dd7f37d3ce53ba', now());

INSERT INTO EVENTLOG VALUES (now(),'dir2', 'mkdir', 1, '/bin/mkdir', 'docker', 'coco_watch');

INSERT INTO WATCHES VALUES ('test_watch', '/home/docker/test_dir/');
INSERT INTO WATCHES VALUES ('coco_watch', '/home/docker/coco_dir/');