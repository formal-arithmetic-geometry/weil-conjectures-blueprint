+++
kind  = "proof"
of    = "prop-weil-filtered-retract-descent"
+++
Let $e:(E,K)\to(E,K)$ be an idempotent of the pair category
$\mathcal P_T$ of [def-weil-pbc-finite-stage-pair-category] and let
$(M,u)$, with $u:T_{M/E}K\to T_{M/E}K$, be a representative of $e$. The
equality $e^2=e$ holds in $\mathcal P_T$, so by the equivalence relation and
the transport formula of [prop-weil-pbc-common-stage-calculus] there is a
finite $P\supset M$ with
$$
 u_P\circ u_P=u_P
 \qquad\text{in }\mathcal C_P(T)
$$
(the composite $e^2$ being represented by $(M,u\circ u)$). The category
$\mathcal C_P(T)=\Dbc(T,P)$ is idempotent complete by the hypothesis
(verified by [thm-weil-pbc-finite-stage-karoubian]), so there exist
$K'_P\in\mathcal C_P(T)$, $p_P:T_{P/E}K\to K'_P$, and
$i_P:K'_P\to T_{P/E}K$ with
$$
 p_P\,i_P=\operatorname{id}_{K'_P},\qquad i_P\,p_P=u_P.
$$
In $\mathcal P_T$, let $K'=(P,K'_P)$, and let
$$
 i=[P,i_P]:K'\longrightarrow(P,T_{P/E}K)\cong(E,K),
\qquad
 p=[P,p_P]:(E,K)\cong(P,T_{P/E}K)\longrightarrow K',
$$
where the displayed isomorphisms are the classes of the identity morphisms
(well defined, since $P\supset E$). Then $p\,i=[P,p_P\,i_P]$ is the class of
the identity, i.e. the identity of $K'$, and $i\,p=[P,i_P\,p_P]=[P,u_P]$ is
the class of $e$. Hence $e$ splits in $\mathcal P_T$, over the single field
$P$.
