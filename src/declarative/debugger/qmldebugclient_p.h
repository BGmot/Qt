/****************************************************************************
**
** Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
** All rights reserved.
** Contact: Nokia Corporation (qt-info@nokia.com)
**
** This file is part of the QtDeclarative module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL$
** No Commercial Usage
** This file contains pre-release code and may not be distributed.
** You may use this file in accordance with the terms and conditions
** contained in the Technology Preview License Agreement accompanying
** this package.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 2.1 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL included in the
** packaging of this file.  Please review the following information to
** ensure the GNU Lesser General Public License version 2.1 requirements
** will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
**
** In addition, as a special exception, Nokia gives you certain additional
** rights.  These rights are described in the Nokia Qt LGPL Exception
** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
**
** If you have questions regarding the use of this file, please contact
** Nokia at qt-info@nokia.com.
**
**
**
**
**
**
**
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef QMLDEBUGCLIENT_H
#define QMLDEBUGCLIENT_H

#include <QtNetwork/qtcpsocket.h>

QT_BEGIN_HEADER

QT_BEGIN_NAMESPACE

QT_MODULE(Declarative)

class QmlDebugConnectionPrivate;
class Q_DECLARATIVE_EXPORT QmlDebugConnection : public QTcpSocket
{
    Q_OBJECT
    Q_DISABLE_COPY(QmlDebugConnection)
public:
    QmlDebugConnection(QObject * = 0);

    bool isConnected() const;
private:
    QmlDebugConnectionPrivate *d;
    friend class QmlDebugClient;
    friend class QmlDebugClientPrivate;
};

class QmlDebugClientPrivate;
class Q_DECLARATIVE_EXPORT QmlDebugClient : public QObject
{
    Q_OBJECT
    Q_DECLARE_PRIVATE(QmlDebugClient)
    Q_DISABLE_COPY(QmlDebugClient)

public:
    QmlDebugClient(const QString &, QmlDebugConnection *parent);

    QString name() const;

    bool isEnabled() const;
    void setEnabled(bool);

    bool isConnected() const;

    void sendMessage(const QByteArray &);

protected:
    virtual void messageReceived(const QByteArray &);

private:
    friend class QmlDebugConnection;
    friend class QmlDebugConnectionPrivate;
};

QT_END_NAMESPACE

QT_END_HEADER

#endif // QMLDEBUGCLIENT_H