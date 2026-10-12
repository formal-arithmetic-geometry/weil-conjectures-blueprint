+++
kind  = "proof"
of    = "lemma-weil-pbc-gabber-effacement"
+++
Apply constructible approximation to obtain a constructible $C$ with a
morphism $\iota:C\to F$ through which $c$ factors (in general $\iota$ is not
a monomorphism), and use finite-pushforward reduction to choose

$$
C\hookrightarrow D_0=\bigoplus_{i=1}^r(h_i)_*\underline{M_i}.
$$

Let $c_i$ be the image of $c$ in
$H^q(T_0,(h_i)_*\underline{M_i}|_{T_0})$. Finite direct-image exactness
identifies $c_i$ with a class on the closed fibre of $h_i$. Apply finite-cover
killing to each $c_i$ and take the fibre product of the resulting finite
covers over $T$; after replacing by one finite-presentation stage, call the
common finite cover $h:V\to T$. Every component of $h_0^*c$ is zero.
The composite unit

$$
C\hookrightarrow D_0\longrightarrow h_*h^*D_0=:D
$$

is monic by the finite stalk product formula. Form the pushout square

$$
\begin{CD}
C @>>> D\\
@VVV @VVV\\
F @>>> F':=F\amalg_C D.
\end{CD}
$$

Pushout monicity, which needs only $C\to D$ to be monic, makes $F\to F'$
injective. The image of $c$ in
$H^q(T_0,D_0)$ is carried to zero in $H^q(T_0,D)$ because its pullback to
$V_0$ is zero and $h_*$ is exact. The pushout square therefore carries $c$
to zero in $H^q(T_0,F'_0)$.
