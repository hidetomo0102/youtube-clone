import { React, useContext } from "react";
import { makeStyles } from "@material-ui/styles";
import {
  Typography,
  Card,
  CardMedia,
  CardContent,
  CardActionArea,
} from "@material-ui/core";

import { ApiContext } from "../context/ApiContext";

const useStyles = makeStyles((theme) => ({
  card: {
    position: "relative",
    display: "flex",
    marginBottom: 15,
  },
  cardcontext: {
    padding: theme.spacing(1),
  },
}));

const VideoItem = ({ video }) => {
  const classes = useStyles();
  const { setSelectedVideo } = useContext(ApiContext);

  return (
    <Card className={classes.card} onClick={() => setSelectedVideo(video)}>
      <CardActionArea>
        <CardMedia
          component="img"
          alt="thumbnail"
          height="200"
          image={video.thumbnail}
        />
        <CardContent className={classes.cardcontext}>
          <Typography variant="h6">{video.title}</Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
};

export default VideoItem;
