+++
kind  = "proof"
of    = "lemma-nagata-conrad-case3-disjointness-reduction"
uses = ["def-nagata-qc-open-complement-ideal", "def-nagata-extended-ideal", "lemma-nagata-conrad-disjointness-blowup", "lemma-nagata-qc-open-complement-ideal-exists", "lemma-nagata-finite-type-ideal-compact", "lemma-nagata-finite-type-ideal-power-in-ideal", "lemma-nagata-ideal-directed-union-finite-type"]
+++
We produce the two ideals $\mathcal I_1,\mathcal I_2$ required by
[lemma-nagata-conrad-disjointness-blowup], applied to the opens
$U\subseteq V\subseteq X$, to $p\colon Y\to X$ in the role of $Z\to X$, and
to $f\colon U\to Y$ in the role of the morphism whose source lies over
$U$ (indeed $p\circ f$ is the inclusion of $U$). The morphism $f$ is
quasi-compact, since $U$ is quasi-compact and $Y$ is quasi-separated, so
its scheme-theoretic image $\overline{f(U)}$ has underlying set the
closure of $f(U)$.

Let $\mathcal H$ be the ideal of the reduced structure on the closed subset
$\overline{V\setminus U}$, so $V(\mathcal H)=\overline{V\setminus U}$; since
$V\setminus U$ is closed in $V$, its closure misses $U$. Give $X\setminus V$
a finite type closed subscheme structure $V(\mathcal K)$ using
[lemma-nagata-qc-open-complement-ideal-exists].

We first check $p\bigl(p^{-1}(V(\mathcal H^2))\cap\overline{f(U)}\bigr) \subseteq X\setminus V$ as sets. Indeed a point of the left-hand side lies
in $\overline{V\setminus U}$, and if it lay in $V$ then, $f(U)$ being closed
in $p^{-1}(V)$, the point of $\overline{f(U)}$ above it would lie in $f(U)$
and so map into $U$, which is disjoint from $\overline{V\setminus U}$. As
$\mathcal K$ is of finite type,
[lemma-nagata-finite-type-ideal-power-in-ideal] gives an $n$ with

$$
\mathcal K^n\cdot\mathcal O_Y\subseteq
\mathcal H^2\cdot\mathcal O_Y+\mathcal I_{\overline{f(U)}} .
$$

The ideal $\mathcal H$ need not be of finite type. By
[lemma-nagata-ideal-directed-union-finite-type] it is the directed
supremum of its finite type quasi-coherent subideals $\mathcal I_{1,\alpha}$;
products and inverse images of ideals commute with directed suprema, so
$\mathcal H^2\cdot\mathcal O_Y+\mathcal I_{\overline{f(U)}}$ is the directed
supremum of the $\mathcal I_{1,\alpha}^2\cdot\mathcal O_Y+ \mathcal I_{\overline{f(U)}}$, and
[lemma-nagata-finite-type-ideal-compact] applied to the finite type
ideal $(\mathcal K\cdot\mathcal O_Y)^n$ produces an $\alpha$ with

$$
\mathcal K^n\cdot\mathcal O_Y\subseteq
\mathcal I_{1,\alpha}^2\cdot\mathcal O_Y+\mathcal I_{\overline{f(U)}} .
$$

Now take $\mathcal I_1=\mathcal I_{1,\alpha}$ and
$\mathcal I_2=\mathcal I_{1,\alpha}^2+\mathcal K^n$, so that
$T_2=V(\mathcal I_2)=T_1\cap V(\mathcal K^n)$ is disjoint from $V$, and
$\mathcal I=\mathcal I_1+\mathcal I_2$. The centre $\mathcal I$ is of finite
type and $V(\mathcal I)\subseteq V(\mathcal I_2)\subseteq X\setminus V$, so
the blow-up is $V$-admissible. The hypotheses of
[lemma-nagata-conrad-disjointness-blowup] hold: $V\setminus U\subseteq
\overline{V\setminus U}=V(\mathcal H)\subseteq V(\mathcal I_{1,\alpha})$
because $\mathcal I_{1,\alpha}\subseteq\mathcal H$; $V(\mathcal I_2)\cap V=\varnothing$;
$p(f(U))=U$ because $f$ is a section of $p$; and
$\mathcal I_2\mathcal O_Y=\mathcal I_{1,\alpha}^2\mathcal O_Y+\mathcal K^n\mathcal O_Y
\subseteq\mathcal I_{1,\alpha}^2\mathcal O_Y+\mathcal I_{\overline{f(U)}}$ by
the last display. Its blow-up is $q\colon\widetilde X=\operatorname{Bl}_{\mathcal I}(X)\to X$,
and for every $Z',r,p',Y',f_Y,f'$ as in the statement (where
$f_Y\colon Y'\to U$ and $r\circ f'=f\circ f_Y$) it gives that
$\overline{f'(Y')}$ is disjoint from
$p'^{-1}\bigl(\overline{q^{-1}(V\setminus U)}\bigr)$, which is the
assertion.

(Conrad additionally arranges $\mathcal I_{1,\alpha}|_U=\mathcal O_U$; this
is not needed here, because $V(\mathcal I)\subseteq V(\mathcal K^n)$ is
already disjoint from $V$, hence from $U$.)
