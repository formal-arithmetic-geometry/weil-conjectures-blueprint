+++
kind  = "proof"
of    = "det-cor-jacobian-torsion-pic"
uses = ["lem-sc-mult-n-isogeny", "sk-prop-av-isogeny", "lem-sc-isogeny-surjective", "sk-cor-picard-degree", "sk-thm-picard-main"]
+++
Write $J=J(C)$; it is an abelian variety over $k$ by [sk-thm-picard-main].

*(1)* By [lem-sc-mult-n-isogeny] and [sk-prop-av-isogeny],
$[n]\colon J\to J$ is finite and surjective. Let $y\in J(k)$, viewed as a
closed point $y\colon\Spec k\to J$. The fibre
$F=J\times_{[n],J,y}\Spec k$ is finite over $\Spec k$ because $[n]$ is
finite, and nonempty because $[n]$ is surjective on underlying points and
$y$ lies in the image. So $F=\Spec B$ with $B$ a nonzero finite
$k$-algebra. For a maximal ideal $\mathfrak m\subset B$, the field
$B/\mathfrak m$ is a finite extension of $k$, hence equal to $k$ since $k$
is algebraically closed. The resulting $k$-point of $F$ is a point
$x\in J(k)$ with $[n](x)=y$, that is $nx=y$ in the group $J(k)$. Thus $J(k)$
is divisible ([lem-sc-isogeny-surjective]).

*(2)* The identity $J[n](k)=J(k)[n]$ holds because $J[n](k)$ is the kernel
of $[n]$ on $J(k)$ (universal property of the kernel). By
[sk-thm-picard-main], $J(k)=\operatorname{Pic}^0(C)$ as groups, and by
[sk-cor-picard-degree] there is an exact sequence of abelian groups
$$
0\longrightarrow J(k)\longrightarrow\operatorname{Pic}(C)\xrightarrow{\ \deg\ }\Z\longrightarrow0.
$$
Apply the snake lemma to the endomorphism "multiplication by $n$" of this
sequence. It gives an exact sequence
$$
0\to J(k)[n]\to\operatorname{Pic}(C)[n]\to\Z[n]\to J(k)/nJ(k)\to\operatorname{Pic}(C)/n\operatorname{Pic}(C)\xrightarrow{\deg}\Z/n\Z\to0 .
$$
Here $\Z[n]=0$ since $\Z$ is torsion free, and $J(k)/nJ(k)=0$ by (1).
Hence $J(k)[n]\to\operatorname{Pic}(C)[n]$ is an isomorphism, i.e. every
$n$-torsion class in $\operatorname{Pic}(C)$ has degree $0$ and lies in
$J(k)[n]$; and $\deg$ induces an isomorphism
$\operatorname{Pic}(C)/n\operatorname{Pic}(C)\simeq\Z/n\Z$.
