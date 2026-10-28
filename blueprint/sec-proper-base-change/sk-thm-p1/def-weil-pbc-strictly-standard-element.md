+++
id = "def-weil-pbc-strictly-standard-element"
kind = "definition"
title = "Elementary standard and strictly standard elements"
lean = ["Algebra.IsStrictlyStandardElement", "Algebra.IsElementaryStandardElement"]
order = 1769
+++
Let $R\to A$ be a ring map of finite presentation and $a\in A$. For a presentation $A=R[x_1,\dots,x_n]/(f_1,\dots,f_m)$ (an isomorphism of $R$-algebras, $f_j\in R[x_1,\dots,x_n]$), write $\partial f_j/\partial x_i$ for the formal partial derivatives and also for their images in $A$. (1) $a$ is *elementary standard in $A$ over $R$* if there are a presentation $A=R[x_1,\dots,x_n]/(f_1,\dots,f_m)$ and an integer $0\le c\le\min(n,m)$ such that $a=a'\det(\partial f_j/\partial x_i)_{i,j=1,\dots,c}$ in $A$ for some $a'\in A$, and $a f_{c+j}\in(f_1,\dots,f_c)+(f_1,\dots,f_m)^2$ for $j=1,\dots,m-c$ (here $a$ stands for any lift of $a$ to $R[x_1,\dots,x_n]$; the condition does not depend on the lift since $(f_1,\dots,f_m)\cdot f_{c+j}\subset(f_1,\dots,f_m)^2$). (2) $a$ is *strictly standard in $A$ over $R$* if there are a presentation $A=R[x_1,\dots,x_n]/(f_1,\dots,f_m)$ and $0\le c\le\min(n,m)$ such that $a=\sum_{I\subset\{1,\dots,n\},\,|I|=c}a_I\det(\partial f_j/\partial x_i)_{j=1,\dots,c,\ i\in I}$ in $A$ for some $a_I\in A$ (columns $i\in I$ in increasing order), and $a f_{c+j}\in(f_1,\dots,f_c)+(f_1,\dots,f_m)^2$ for $j=1,\dots,m-c$.
