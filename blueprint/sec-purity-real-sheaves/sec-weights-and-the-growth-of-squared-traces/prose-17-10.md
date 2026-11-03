+++
id = "prose-17-10"
kind = "hidden"
title = "Weights and the growth of squared traces (3)"
order = 704
+++
In Section [sec-deligne-laumon-a1] we know that the lisse part $M'$
of a Fourier transform is pure, but not of which weight, and the stalk
formula does not show the weight directly. What we do know is its trace function, the discrete
Fourier transform of that of $M$, and Plancherel's formula relates the
sums of squared traces of the two. So we need a number read off from
traces alone that recovers the weight. For a rank-one sheaf pure of
weight $w$ on a curve $U_0$, every $x\in U_0(k_n)$ has
$|\iota t(x)|^2=q^{nw}$, so the sum of squared traces is
$q^{nw}\#U_0(k_n)$. On $\mathbf A^1$ this is exactly $q^{n(w+1)}$, and
on any affine curve it is at most $Dq^{n(w+1)}$ by
Lemma [sk-lem-wrp-point-count]; in rank $r$ the same count gives the upper
bound $r^2Dq^{n(w+1)}$. The number $\nu$ below is this growth
exponent, shifted by $1$ so that it equals the weight. It is a
$\limsup$ because the sums can vanish for infinitely many $n$: on
$\mathcal B_b\oplus\mathcal B_{-b}$ the trace at a point of $U_0(k_n)$ is
$b^n+(-b)^n$, which is $0$ for odd $n$. Theorem [sk-thm-wrp-l2-dictionary]
shows that $\nu$ is the weight of a pure lisse sheaf, and
Theorem [sk-p-dl-a1-fourier-weight] combines this with Plancherel.
