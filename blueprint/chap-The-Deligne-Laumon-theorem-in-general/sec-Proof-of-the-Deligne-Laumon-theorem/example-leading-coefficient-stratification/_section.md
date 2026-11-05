+++
id = "example-leading-coefficient-stratification"
kind = "example"
title = "Why the leading coefficient is inverted"
order = 1359
+++
Let $Y_0=\mathbf A^1_{k_0}=\operatorname{Spec}k_0[y]$, and suppose that $G$
is lisse on the relative line $\mathbf A^1_{Y_0}=\operatorname{Spec}k_0[y,T]$
off the curve $Z=V(yT-1)$. This curve is not finite over the base. Indeed, over a point $y\ne0$ the fibre of $Z$ is the
single point $T=1/y$, and over $y=0$ it is empty, since the equation
becomes $-1=0$. So $Z\to Y_0$ is quasi-finite, but its image
is $D(y)$, which is not closed, whereas a finite map is closed; geometrically, as $y$
tends to $0$ the point $1/y$ runs off to infinity. To repair this, the construction in
the proof takes $g=yT-1$ with leading coefficient $b=y$. Over $D(y)$ the
polynomial $T-y^{-1}$ is monic, and indeed $k_0[y,y^{-1},T]/(yT-1)=k_0[y,y^{-1}]$
is finite over the base. The closed stratum $y=0$, which has smaller
dimension, is treated by induction, and on it the complement of the
lisse locus happens to be empty.
