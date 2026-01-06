from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
X = [[10,5],[50,1],[5,8],[100,0.5]]
y = [1,0,1,0]
model.fit(X,y)

def ai_decision(distance, speed):
    return "MANEUVER" if model.predict([[distance, speed]])[0] else "SAFE"