+++
kind  = "proof"
of    = "det-nagata-common-modification-dense"
uses = ["lemma-nagata-conrad-dense-in-admissible-blowup", "lemma-nagata-admissible-blowup-preserves-density"]
+++
*Step 1: the open is preserved by the modifications.* The blow-up
$\pi_i$ is $j_i(U)$-admissible, so it is an isomorphism over $j_i(U)$ and
$\pi_i^{-1}(j_i(U))=u_i(U)$. In the situation of the second assertion
$u_i$ is moreover quasi-compact: $\pi_i\circ u_i=j_i$ is quasi-compact and
$\pi_i$ is separated, being proper.

*Step 2: density on each chart.* If $j_i(U)$ is dense in $T_i$, the first
assertion of [lemma-nagata-conrad-dense-in-admissible-blowup] shows that
$u_i(U)=\pi_i^{-1}(j_i(U))$ is dense in $T_i'$. If $j_i(U)$ is
scheme-theoretically dense in $T_i$, then
[lemma-nagata-admissible-blowup-preserves-density] shows that $u_i(U)$ is
scheme-theoretically dense in $T_i'$.

*Step 3: topological density in $T$.* The opens $k_1(T_1'),k_2(T_2')$ cover
$T$. Let $O\subseteq T$ be a nonempty open. Then $O\cap k_i(T_i')\ne
\varnothing$ for some $i$, and $k_i^{-1}(O)$ is a nonempty open of $T_i'$, so
it meets $u_i(U)$ by Step 2. Hence $O$ meets $k_i(u_i(U))=j(U)$, and $j(U)$
is dense in $T$.

*Step 4: scheme-theoretic density in $T$.* Injectivity of
$\mathcal O_T\to j_*\mathcal O_U$ is a local property on $T$, so it suffices
to check it on each open $k_i(T_i')$. Since $j(U)\subseteq k_i(T_i')$, the
restriction of $j$ to this open is $k_i\circ u_i$, and under the isomorphism
$k_i:T_i'\xrightarrow{\sim}k_i(T_i')$ the restricted map becomes
$\mathcal O_{T_i'}\to u_{i,*}\mathcal O_U$, which is injective by Step 2.
