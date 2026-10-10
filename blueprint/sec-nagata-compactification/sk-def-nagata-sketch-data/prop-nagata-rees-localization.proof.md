+++
kind  = "proof"
of    = "prop-nagata-rees-localization"
+++
Write $R=\mathcal R_A(I)$ and $R'=\mathcal R_B(J)$, and identify $B$ with
$A_s$.

**Step 1: $R'$ is the localization of $R$ at the degree-zero element $s$.**
For each $n$, let $\rho_{s,n}$ be the equivalence
$A_s\otimes_AR_n\cong R'_n$ of [lemma-nagata-localization-rees-piece]; it
is induced by $\rho_\varphi$ in degree $n$. Taking their direct sum is
legitimate because every Rees element has finite homogeneous support. On
homogeneous tensors of degrees $m,n$, both ways around the multiplication
square have coefficient $(xy)/1$ in degree $m+n$; the equality of localized
ideal powers from [lemma-nagata-localization-ideal-pow] proves
multiplicativity. The direct sum of the inverse maps is constructed in the
same way, and the two composites are identities in each degree, hence on
finite sums. Thus $\rho_\varphi$ induces a graded ring isomorphism
$A_s\otimes_AR\cong R'$, i.e. $R'=R[1/s]$ with $s$ placed in degree zero.

**Step 2: the charts.** Let $a\in I$, so $x=at\in R_1$ and
$\rho_\varphi(x)=\varphi(a)t$. An element of $R'_{(\varphi(a)t),0}$ is a
fraction $y/(\varphi(a)t)^m$ with $y\in R'_m$; by Step 1,
$y=z/s^k$ with $z\in R_m$, so the element is the image of
$z/x^m\in R_{(x),0}$ divided by the image of $s^k$. Conversely the image of
$s$ in $R'_{(\varphi(a)t),0}$ is a unit, and an element $z/x^m$ of
$R_{(x),0}$ maps to zero exactly when $s^kz$ is killed by a power of $x$
in $R$ for some $k$, i.e. when it is killed by a power of $s$ in
$R_{(x),0}$. Since $s$ has degree zero, inverting $s$ commutes with
forming the degree-zero homogeneous localization at $x$, and these two
observations say exactly that $R_{(x),0}\to R'_{(\varphi(a)t),0}$ is a
localization away from the image of $s$.
