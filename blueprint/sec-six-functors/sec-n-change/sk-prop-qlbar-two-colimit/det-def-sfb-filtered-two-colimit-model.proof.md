+++
kind = "proof"
of = "det-def-sfb-filtered-two-colimit-model"
+++
**The colimit is filtered.** The set $\{k\in I:k\ge i,j\}$ is nonempty and directed because $I$ is
directed. By normalization $t_{kk}=\mathrm{id}$, and for $k\le k'\le k''$,
$$
t_{k'k''}t_{kk'}(g)=\tau_{jk'k''}T_{k'k''}(\tau_{jkk'})\,T_{k'k''}T_{kk'}(g)\,T_{k'k''}(\tau_{ikk'})^{-1}\tau_{ik'k''}^{-1}
=\tau_{jkk''}\,T_{kk''}(g)\,\tau_{ikk''}^{-1}=t_{kk''}(g),
$$
using the cocycle identity at $x$ (indices $i\le k\le k'\le k''$) and at $y$ (indices
$j\le k\le k'\le k''$), and naturality of $\tau_{kk'k''}\colon T_{k'k''}T_{kk'}\Rightarrow T_{kk''}$. So $(H_k,t_{kk'})$ is a functor on a
directed set, and $[k,g]=[k',g']$ if and only if $t_{km}(g)=t_{k'm}(g')$ for some $m\ge k,k'$.

**Composition.** Each $t_{mm'}$ preserves composition and identities, being conjugation of the
functor $T_{mm'}$ by isomorphisms. Hence $[m,t_{k'm}(h)t_{km}(g)]$ does not change when $m$ is
replaced by $m'\ge m$, so any two choices of $m$ give the same class (pass to a common upper bound).
Replacing $g$ by $t_{kn}(g)$ or $h$ by $t_{k'n}(h)$ does not change the result either, by
$t_{nm}t_{kn}=t_{km}$; so composition is well defined. Associativity and unitality follow by computing
all composites at one common stage $m$, where they are associativity and unitality in
$\mathcal C_m$, and $t_{im}(\mathrm{id}_x)=\mathrm{id}$.

**The comparison functor.** For $k\le k'$, compatibility gives
$\theta_{ik',x}^{-1}=\Phi_{k'}(\tau_{ikk',x})\circ\theta_{kk',T_{ik}x}^{-1}\circ\theta_{ik,x}^{-1}$, and
similarly for $y$. Therefore
$$
\theta_{jk',y}\Phi_{k'}(t_{kk'}g)\theta_{ik',x}^{-1}
=\theta_{jk,y}\,\theta_{kk',T_{jk}y}\,\Phi_{k'}T_{kk'}(g)\,\theta_{kk',T_{ik}x}^{-1}\,\theta_{ik,x}^{-1}
=\theta_{jk,y}\Phi_k(g)\theta_{ik,x}^{-1},
$$
by naturality of $\theta_{kk'}\colon\Phi_{k'}T_{kk'}\Rightarrow\Phi_k$. So $\Phi$ is well defined on
classes. It sends $[i,\mathrm{id}_x]$ to $\theta_{ii}\Phi_i(\mathrm{id})\theta_{ii}^{-1}=\mathrm{id}$, and,
computing a composite at a common stage $m$,
$\Phi([m,h_m])\Phi([m,g_m])=\theta_{lm,z}\Phi_m(h_m)\theta_{jm,y}^{-1}\theta_{jm,y}\Phi_m(g_m)\theta_{im,x}^{-1}=\Phi([m,h_mg_m])$.
