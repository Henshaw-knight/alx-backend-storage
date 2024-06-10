-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS u
    SET u.average_score = (
	SELECT
	    CASE
		WHEN SUM(b.weight) > 0 THEN SUM(a.score * b.weight) / SUM(b.weight)
		ELSE 0
	    END
	FROM corrections AS a INNER JOIN projects AS b
	ON b.id = a.project_id
	WHERE a.user_id = u.id
    );
END $$

DELIMITER ;
