+++
kind = "proof"
of = "corollary-continuity-cohomology"
order = 107
+++
We compute both sides with one hypercover by weakly contractible affines,
chosen independently of $i$. Because of the common lower bound $a$, each
total degree $q$ of (2.3) is a finite sum, of the
terms $K_i^{q-r}(W_r)$ with $0\leq r\leq q-a$, and the range of $r$ is the
same for all $i$.

By Corollary [corollary-evaluation-weakly-contractible-objects], sections on each $W_r$ commute with
filtered colimits, hence so does the finite sum in each total
degree of (2.3), and the hypercover complex of
$\varinjlim_iK_i^\bullet$ is the filtered colimit of the hypercover
complexes of the $K_i^\bullet$. The first assertion follows because
filtered colimits of modules are exact and so commute with cohomology.

The second assertion reduces to the first. Recall that $R^qf_*K$ is the
sheaf associated to the presheaf $V\mapsto H^q(X\times_YV,K)$, and that
the affine objects $V$ of $Y_{\mathrm{pro}\acute{e}t}$ form a basis. For such $V$ the
object $X\times_YV$ is quasi-compact and quasi-separated, so the first
assertion applies to it, and sheafification commutes with colimits.
