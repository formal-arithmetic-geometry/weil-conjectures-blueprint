+++
kind = "proof"
of = "sk-thm-iff"
uses = ["sk-def-exchange", "sk-thm-acyclicity", "sk-prop-pbc-degree-zero"]
+++
Condition (i) implies (ii) by placing $F$ in degree zero. Suppose (ii)
holds and $I$ is an injective sheaf of $\Lambda$-modules. Then
$R^qf_*I=0$ for $q>0$, and (ii) applied to $I$ gives
$R^qf'_*g'^*I\simeq g^*R^qf_*I=0$ for $q>0$.
This proves (iii).

Now assume (iii), let $F$ be a sheaf of $\Lambda$-modules, and choose an
injective resolution $F\to I^\bullet$ by sheaves of $\Lambda$-modules.
Since $g'^*$ is exact, $g'^*I^\bullet$ is a resolution of $g'^*F$, and by (iii) its
terms are $f'_*$-acyclic. Hence Lemma [sk-thm-acyclicity] identifies
$f'_*g'^*I^\bullet$ with $Rf'_*g'^*F$. The complex
$g^*f_*I^\bullet$ computes $g^*Rf_*F$ because inverse image
is exact. Proposition [sk-prop-pbc-degree-zero] provides an isomorphism

$$
g^*f_*I^m\xrightarrow{\sim} f'_*g'^*I^m
$$

in each degree. By naturality these form an isomorphism of complexes,
which by (4.4) is the derived base change map
for $F$. This proves (ii).

Finally, let $K\in D^+(X_{\acute{e}t},\Lambda)$. If $K$
is bounded, then by induction on its cohomological length, using the
canonical truncation triangles and (ii), we see that its base change map is an
isomorphism. In general, we fix a degree $m$ and choose $N\geq m$.
The complex $\tau_{\leq N}K$ is bounded and has the desired
comparison. Both functors $g^*Rf_*$ and $Rf'_*g'^*$ send
$D^{\geq N+1}(X_{\acute{e}t},\Lambda)$ into $D^{\geq N+1}(Y'_{\acute{e}t},\Lambda)$, since inverse images are exact
and derived direct images are left $t$-exact. Applying them to

$$
\tau_{\leq N}K\longrightarrow K\longrightarrow
\tau_{\geq N+1}K\xrightarrow{+1}
$$

we see that the comparison for $K$ in degree $m$ is the comparison for
$\tau_{\leq N}K$, which is an isomorphism. Since $m$ was arbitrary,
(i) follows.
