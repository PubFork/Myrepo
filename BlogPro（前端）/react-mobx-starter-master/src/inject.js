import React from 'react';

const inject=service=>Component=>props=><Component {...service} {...props}/> ;

export default inject;
