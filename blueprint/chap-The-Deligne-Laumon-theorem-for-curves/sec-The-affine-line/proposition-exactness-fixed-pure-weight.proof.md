+++
kind = "proof"
of = "proposition-exactness-fixed-pure-weight"
order = 1296
uses = ["proposition-pro-etale-coverings", "proposition-weights-j-boundary-points", "lemma-local-duality-point-c-u"]
+++
Applying $j_*$ to the short exact sequence gives the long exact sequence

$$
0\to j_*F_1\to j_*F\to j_*F_2\xrightarrow{\ \delta\ }R^1j_*F_1,
$$

so it suffices to show that the connecting map $\delta$ vanishes. It is
Frobenius-equivariant, and we show that its source and target have
disjoint weights.
Since $R^1j_*F_1$ is zero on $U$, we look at a point of
$C\setminus U$. There the stalk of the source has weights at most $w$
by Proposition [proposition-weights-j-boundary-points]. For the target, note that the dual
$F_1^\vee$ is pure of weight $-w$, so the same result shows that the
stalk of $j_*F_1^\vee$ has weights at most $-w$. By
Lemma [lemma-local-duality-point-c-u] the stalk of the target is
the dual of this stalk twisted by $(-1)$, and hence the target has weights
at least $w+2$. Now the image of $\delta$ is a
quotient of the source and a submodule of the target, so its
eigenvalues would have weights both at most $w$ and at least $w+2$.
Hence $\delta$ vanishes at each point of $C\setminus U$. As
$R^1j_*F_1$ is zero on $U$, it follows that $\delta=0$.
