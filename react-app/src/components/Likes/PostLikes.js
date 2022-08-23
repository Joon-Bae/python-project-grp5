import { useState, useEffect } from "react"
import { useDispatch, useSelector } from 'react-redux'
import { Link, Redirect, useHistory } from 'react-router-dom'
import heartImage from '../../Images/svgexport-3.svg'
import '../posts/post.css'

export default function PostLikes( { postId }) {

    return (
        <div className="post-likes-container">
        <img className="post-like-button" src={ heartImage } alt=''/>
        </div>
    )
}
