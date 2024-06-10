-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE weighted_sum FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    DECLARE average_weighted_score FLOAT DEFAULT 0;

    SELECT
        SUM(a.score * b.weight),
	SUM(b.weight)
    INTO
        weighted_sum,
	total_weight
    FROM corrections AS a
    INNER JOIN projects as b ON b.id = a.project_id
    WHERE a.user_id = user_id;

    IF total_weight > 0 THEN
	SET average_weighted_score = weighted_sum / total_weight;
    END IF;

    UPDATE users
    SET average_score = average_weighted_score
    WHERE id = user_id;
END $$

DELIMITER ;
