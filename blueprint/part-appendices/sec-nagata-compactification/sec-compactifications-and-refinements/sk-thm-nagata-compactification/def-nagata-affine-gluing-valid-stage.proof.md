+++
kind  = "proof"
of    = "def-nagata-affine-gluing-valid-stage"
uses = ["lemma-nagata-finite-affine-gluing-presentation", "pqf-lem-limit-qc-open-descends", "prop-nagata-noetherian-inverse-system"]
+++
Cofinality. Let $T_a\subseteq\Gamma(S,U_a)$ be finite sets. The scheme $S$
is quasi-compact and quasi-separated, since it is covered by finitely many
affine charts whose overlaps are quasi-compact
([lemma-nagata-finite-affine-gluing-presentation]). By
[prop-nagata-noetherian-inverse-system] choose a Noetherian approximation
$S=\varprojlim_k S_k$. By [pqf-lem-limit-qc-open-descends] each chart
$U_a$ is the preimage of a quasi-compact open of some stage, which becomes
affine after passing to a later stage (Stacks, Tag 01Z6); as there are
finitely many charts, there are one stage $k_0$ and affine opens
$V_a\subseteq S_{k_0}$ with preimage $U_a$. Since $U_a$ is the limit of
the affine preimages of $V_a$ in the later stages, $\Gamma(S,U_a)$ is the
filtered colimit of their section rings; hence the finitely many elements
of $T_a$ and the witnesses of the chart $a$ (among them the $f_{abr}$ and
$g_{bar}$) are images of sections over the preimage of $V_a$ at a single
stage $k_1$. The basic opens of the chosen lifts $f'_{abr}$ and $g'_{abr}$
have the same preimage $D(f_{abr})=D(g_{abr})$ in $S$, so by
[pqf-lem-limit-qc-open-descends] they agree at a later stage $k_2$.

Let $A_a\subseteq\Gamma(S,U_a)$ be the image of the sections over the
preimage of $V_a$ at $k_2$. This is a quotient of a finitely generated
$\mathbf Z$-algebra, because $S_{k_2}$ is of finite type over $\mathbf Z$,
so $A_a$ is finitely generated; it contains $T_a$ and the witnesses, so
the three unit conditions hold. The localization subring
$A_a[1/f_{abr}]$ is the image of the sections over the basic open of
$f'_{abr}$ at $k_2$, and $A_b[1/g_{abr}]$ is the image of the sections
over the basic open of $g'_{abr}$, which is the same open of $S_{k_2}$;
so the two localization subrings agree. Hence $(A_a)_a$ is a valid stage
containing every $T_a$.

The selected stage $\lambda_{\mathrm{glue}}(S)$ exists by cofinality
applied to the finite generating sets of the $A^{\mathrm{coeff}}_a$.
