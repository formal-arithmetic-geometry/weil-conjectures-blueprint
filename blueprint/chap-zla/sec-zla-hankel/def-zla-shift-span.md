+++
id = "def-zla-shift-span"
kind = "definition"
title = "Shift span and Hankel matrix"
order = 998
+++
For a sequence $a=(a_n)_{n\geq0}\in K^{\mathbf N}$, define the left shift $Sa$
by $(Sa)_n=a_{n+1}$, and put

$$
\operatorname{Sh}_K(a)=\Span_K\{S^ma:m\geq0\}\subseteq K^{\mathbf N}.
$$

The associated Hankel matrix is $H(a)=(a_{r+s})_{r,s\geq0}$; its columns are
the shifts of $a$. It has rank at most $h$ if every $(h+1)\times(h+1)$ minor
$\det(a_{r_x+s_y})_{0\leq x,y\leq h}$ vanishes, for all choices of nonnegative
indices $r_x,s_y$.
