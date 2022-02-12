CREATE TABLE userData (
    userID INT NOT NULL,
    phoneNo VARCHAR(20)
)

CREATE TABLE channelData (
    channelID INT NOT NULL,
    userID INT NOT NULL,
    FOREIGN KEY (userID) REFERENCES userData (userID)
)