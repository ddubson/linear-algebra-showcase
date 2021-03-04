# Unit vectors
v1 = [-3 6]

# m*u
mu = 1/norm(v1)

# Plot
figure(5), clf

plot([0 v1(1)],[0 v1(2)],'b','linew',2)
hold on
plot([0 v1(1)]*mu,[0 v1(2)]*mu,'r:','linew', 4)
legend({'v1';'v1-unit'})

axis square
axis([-1 1 -1 1]*norm(v1))
hold on
plot(get(gca,'xlim'),[0 0],'k--')
plot([0 0],get(gca,'ylim'),'k--')
xlabel('X_1 dimension')
ylabel('X_2 dimension')